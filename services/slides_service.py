from datetime import datetime
from random import randint

from utils.file_handlers.docx_handler import DocxHandler
from utils.file_handlers.pdf_handler import PdfHandler
from utils.ai.models import generate_text_4o, generate_text_4o_mini, generate_image_url
from utils.slides.slide_generator import (
    create_slide,
    init_presentation,
    save_presentation,
)
from utils.slides.xml_to_dict import xml_to_slides_dict, slides_dict_to_xml
import utils.ai.prompts as PROMPTS


class SlideService:
    def __init__(self):
        self.docx_handler = DocxHandler()
        self.pdf_handler = PdfHandler()

    def get_outline(self, file, user_input: str) -> dict[str, str]:
        content = ""
        if file and user_input:
            file_extension = file.filename.split(".")[-1].lower()
            if file_extension == "docx":
                content = f"{user_input}\nTham khảo nội dung tài liệu dưới: {self.docx_handler.extract_text(file)}"
            elif file_extension == "pdf":
                content = f"{user_input}\nTham khảo nội dung tài liệu dưới: {self.pdf_handler.extract_text(file)}"
            print(content)
        elif file:
            file_extension = file.filename.split(".")[-1].lower()
            if file_extension == "docx":
                content = self.docx_handler.extract_text(file)
            elif file_extension == "pdf":
                content = self.pdf_handler.extract_text(file)
        else:
            content = user_input

        prompt = PROMPTS.outline.format(content=content)
        outline = generate_text_4o(prompt)
        outline = outline.split("- ")[1:]
        return {"outline": outline, "content": content}

    def get_slide_content(self, outline: str, content: str) -> str:
        prompt = PROMPTS.content.format(outline=outline, content=content)
        content = generate_text_4o(prompt)
        with open("slides.xml", "w") as f:
            f.write(content)
        content = xml_to_slides_dict(content)
        return {"content": content}

    def create_slide(self, slides: list, template_name: str = "Facet"):
        slides_str = slides_dict_to_xml(slides_list=slides)
        with open("slides.xml", "w") as f:
            f.write(slides_str)

        def get_img_url(_slide_content, img_description):
            _prompt = PROMPTS.illustration.format(
                slide_content=_slide_content, img_description=img_description
            )
            _prompt = generate_text_4o_mini(_prompt)
            return generate_image_url(_prompt)

        prompt = PROMPTS.file_name.format(slide_content=slides_str)
        output_file_name = generate_text_4o_mini(prompt)
        output_file_name = f"{output_file_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{randint(0, 9999)}.pptx"
        prs = init_presentation(template_name)
        for slide in slides:
            layout = slide["layout"]
            if "image_path" in slide:
                slide["image_path"] = get_img_url(
                    _slide_content=slides_str, img_description=slide["image_path"]
                )
            print("Creating slide with layout:", layout)
            create_slide(prs, layout, **slide)

        save_presentation(prs, output_file_name)
        return {"file_name": output_file_name}
