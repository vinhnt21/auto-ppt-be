from .base_handler import BaseSubjectHandler
from utils.ai.subject_prompts.civics_prompts import CIVICS_PROMPTS
from utils.ai.models import generate_text_4o


class CivicsHandler(BaseSubjectHandler):
    def get_outline(self, content: str, subject: str) -> str:
        prompt = CIVICS_PROMPTS['outline'].format(content=content)
        return generate_text_4o(prompt)

    def get_slide_content(self, outline: str,  content: str) -> str:
        prompt = CIVICS_PROMPTS['content'].format(outline=outline)
        return generate_text_4o(prompt)

    def get_illustration(self, slide_content: str, content: str, subject: str):
        prompt = CIVICS_PROMPTS['illustration'].format(
            slide_content=slide_content,
            content=content
        )
        return generate_text_4o(prompt)

    def create_slide(self, slide_content: str, content: str, subject: str):
        # Implement slide creation logic
        pass
