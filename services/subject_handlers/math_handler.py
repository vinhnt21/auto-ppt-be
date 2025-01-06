from .base_handler import BaseSubjectHandler
from utils.ai.models import generate_text_4o, generate_text_4o_mini, generate_image_url
import utils.ai.subject_prompts.math_prompts as MATH_PROMPTS
from utils.slides.slide_generator import *


class MathHandler(BaseSubjectHandler):
    def get_outline(self, content: str, subject: str) -> str:
        prompt = MATH_PROMPTS.outline.format(content=content)
        outline = generate_text_4o(prompt)
        outline = outline.split('- ')[1:]
        return outline

    def get_slide_content(self, outline: str, content: str) -> list[str]:
        prompt = MATH_PROMPTS.content.format(outline=outline, content=content)
        content = generate_text_4o(prompt)
        with open('_content.md', 'w') as f:
            f.write(content)
        prompt = MATH_PROMPTS.layout.format(outline=outline, generated_content=content)
        content = generate_text_4o(prompt)
        with open('_layout.txt', 'w') as f:
            f.write(content)
        return content

    def get_illustration(self, slide_content: str, content: str, subject: str):
        prompt = MATH_PROMPTS.illustration.format(
            slide_content=slide_content,
            content=content
        )
        return generate_text_4o(prompt)

    def create_slide(self, slide_content: str, subject: str):
        def _convert_str_to_dict(s):
            s = s.split("\n")
            s = [line for line in s if line.strip() != ""]
            res = {}
            for i in s:
                components = i.split("***")
                components = [component.strip() for component in components if component.strip() != ""]
                for component in components:
                    try:
                        key, value = component.split(":", 1)
                        res[key.strip()] = value.strip().strip('"')
                    except ValueError:
                        print(f"Warning: Skipping invalid line: {component}")
                        continue
            return res

        def get_img_url(_slide_content, img_description):
            _prompt = MATH_PROMPTS.illustration.format(
                slide_content=_slide_content,
                img_description=img_description
            )
            _prompt = generate_text_4o_mini(_prompt)
            return generate_image_url(_prompt)


        prompt = MATH_PROMPTS.file_name.format(slide_content=slide_content)
        output_file_name = generate_text_4o_mini(prompt)

        prs = init_presentation()
        slides = slide_content.strip().strip("---").split("---\n")
        slides = [slide for slide in slides if slide]
        for slide in slides:
            dict_slide = _convert_str_to_dict(slide)

            layout = dict_slide["layout"]
            # if dict_slide contains image
            if "image_path" in dict_slide:
                dict_slide["image_path"] = get_img_url(slide_content, dict_slide["image_path"])
                print(dict_slide["image_path"])
            create_slide(prs, layout, **dict_slide)
        apply_global_styles(prs, "vibrant")
        save_presentation(prs, output_file_name)
        return output_file_name
