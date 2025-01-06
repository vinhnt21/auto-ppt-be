from services.subject_handlers.math_handler import MathHandler
from services.subject_handlers.civics_handler import CivicsHandler
from services.subject_handlers.base_handler import BaseSubjectHandler
from utils.file_handlers.docx_handler import DocxHandler
from utils.file_handlers.pdf_handler import PdfHandler


class SlideService:
    def __init__(self):
        self.docx_handler = DocxHandler()
        self.pdf_handler = PdfHandler()

        self.handlers = {
            'math': MathHandler(),
            'civics': CivicsHandler(),
            'none': BaseSubjectHandler()
        }

    def get_handler(self, subject: str):
        handler = self.handlers.get(subject.lower())
        if not handler:
            raise ValueError(f"No handler for subject: {subject}")
        return handler

    def get_outline(self, file, user_input: str, subject: str) -> dict[str, str]:
        content = ""
        if file and user_input:
            file_extension = file.filename.split('.')[-1].lower()
            if file_extension == 'docx':
                content = f'{user_input}\nTham khảo nội dung tài liệu dưới: {self.docx_handler.extract_text(file)}'
            elif file_extension == 'pdf':
                content = f'{user_input}\nTham khảo nội dung tài liệu dưới: {self.pdf_handler.extract_text(file)}'
            print(content)
        elif file:
            file_extension = file.filename.split('.')[-1].lower()
            if file_extension == 'docx':
                content = self.docx_handler.extract_text(file)
            elif file_extension == 'pdf':
                content = self.pdf_handler.extract_text(file)
        else:
            content = user_input
        handler = self.get_handler(subject)
        return {
            'outline': handler.get_outline(content, subject),
            'content': content
        }

    def get_slide_content(self, outline: str, subject: str, content: str) -> str:
        handler = self.get_handler(subject)
        return handler.get_slide_content(outline, subject)

    def get_illustration(self, slide_content: str, content: str, subject: str):
        handler = self.get_handler(subject)
        return handler.get_illustration(slide_content, content, subject)

    def create_slide(self, slide_content: str, subject: str, template_name: str = 'light'):
        handler = self.get_handler(subject)
        return handler.create_slide(slide_content, subject, template_name)
