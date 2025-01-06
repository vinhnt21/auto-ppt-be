class BaseSubjectHandler:
    def get_outline(self, content: str, subject: str) -> str:
        raise NotImplementedError

    def get_slide_content(self, outline: str, content: str) -> str:
        raise NotImplementedError

    def get_illustration(self, slide_content: str, content: str, subject: str):
        raise NotImplementedError

    def create_slide(self, slide_content: str, subject: str, template_name: str = 'light'):
        raise NotImplementedError
