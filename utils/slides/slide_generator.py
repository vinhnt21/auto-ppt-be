from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_AUTO_SIZE
from pptx.util import Pt
from pptx.util import Inches
import requests
from io import BytesIO
from env_config import SLIDE_FOLDER

# Layout mapping
LAYOUT = {
    'Title Slide': 0,
    'Title and Content': 1,
    'Section Header': 2,
    'Two Content': 3,
    'Comparison': 4,
    'Content with Caption': 7,
    'Picture with Caption': 8,
}


def process_text(text):
    """
    Xử lý text trước khi thêm vào slide
    """
    if not isinstance(text, str):
        return text

    # Thay thế \\n bằng xuống dòng thật
    text = text.replace('\\n', '\n')
    return text


def get_layout(name: str) -> int:
    name = name.strip()
    if name not in LAYOUT:
        raise ValueError(f'Invalid slide layout: {name}')
    return LAYOUT[name]


def init_presentation(template_path=None):
    """
    Khởi tạo đối tượng Presentation với tỷ lệ khung hình 16:9.
    Args:
        template_path: Đường dẫn tới template (mặc định: None)
    Returns:
        prs: Đối tượng Presentation
    """
    prs = Presentation(template_path) if template_path else Presentation()

    # Đặt tỷ lệ khung hình 16:9 (10 x 5.625 inch)
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(5.625)

    return prs


def set_text_frame_properties(text_frame):
    """Thiết lập thuộc tính cho text frame."""
    text_frame.word_wrap = True
    text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE


def style_text(text_frame, font_name="Arial", font_size=20, font_color=(0, 0, 0)):
    """
    Áp dụng kiểu dáng cho một TextFrame với hỗ trợ text nhiều dòng.
    """
    set_text_frame_properties(text_frame)

    # Xử lý từng paragraph
    for paragraph in text_frame.paragraphs:
        paragraph.font.name = font_name
        paragraph.font.size = Pt(font_size)
        paragraph.font.color.rgb = RGBColor(*font_color)

        # Xử lý từng run trong paragraph
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = Pt(font_size)
            run.font.color.rgb = RGBColor(*font_color)


def set_placeholder_text(placeholder, text, font_name="Arial", font_size=20, font_color=(0, 0, 0)):
    """
    Thiết lập text cho placeholder với định dạng
    """
    if placeholder.has_text_frame:
        text_frame = placeholder.text_frame
        text_frame.text = process_text(text)
        style_text(text_frame, font_name, font_size, font_color)


# Các hàm tạo slide
def add_title_slide(prs, title: str, subtitle: str = ""):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Title Slide')])
    slide.shapes.title.text = process_text(title)
    if subtitle:
        slide.placeholders[1].text = process_text(subtitle)
    return slide


def add_title_and_content_slide(prs, title: str, content: str):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Title and Content')])
    slide.shapes.title.text = process_text(title)
    slide.placeholders[1].text = process_text(content)
    return slide


def add_section_header_slide(prs, title: str, subtitle: str = ""):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Section Header')])
    slide.shapes.title.text = process_text(title)
    if subtitle:
        slide.placeholders[1].text = process_text(subtitle)
    return slide


def add_two_content_slide(prs, title: str, left_content: str, right_content: str):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Two Content')])
    slide.shapes.title.text = process_text(title)
    slide.placeholders[1].text = process_text(left_content)
    slide.placeholders[2].text = process_text(right_content)
    return slide


def add_comparison_slide(prs, title: str, left_title: str, left_content: str,
                         right_title: str, right_content: str):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Comparison')])
    slide.shapes.title.text = process_text(title)
    slide.placeholders[1].text = process_text(left_title)
    slide.placeholders[2].text = process_text(left_content)
    slide.placeholders[3].text = process_text(right_title)
    slide.placeholders[4].text = process_text(right_content)
    return slide


def add_content_with_caption_slide(prs, title: str, content: str, caption: str):
    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Content with Caption')])
    slide.shapes.title.text = process_text(title)
    slide.placeholders[1].text = process_text(content)
    slide.placeholders[2].text = process_text(caption)
    return slide


def add_picture_with_caption_slide(prs, title: str, image_path: str, caption: str):
    """
    Thêm slide với hình ảnh và chú thích, hỗ trợ cả đường dẫn local và URL
    """

    def download_image(url):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BytesIO(response.content)
        except Exception as e:
            print(f"Error downloading image from {url}: {e}")
            return None

    slide = prs.slides.add_slide(prs.slide_layouts[get_layout('Picture with Caption')])
    slide.shapes.title.text = process_text(title)
    placeholder = slide.placeholders[1]

    # Kiểm tra nếu image_path là URL
    if image_path.startswith(('http://', 'https://')):
        image_data = download_image(image_path)
        if image_data:
            placeholder.insert_picture(image_data)
        else:
            # Có thể thêm hình ảnh placeholder hoặc thông báo lỗi
            placeholder.text = "Failed to load image"
    else:
        # Xử lý đường dẫn local như bình thường
        placeholder.insert_picture(image_path)

    slide.placeholders[2].text = process_text(caption)
    return slide


def create_slide(prs, layout_name, **kwargs):
    """
    Hàm điều phối để tạo slide dựa trên layout.
    """
    layout_name = layout_name.strip()

    if layout_name == 'Title Slide':
        return add_title_slide(prs, kwargs.get('title', ''), kwargs.get('subtitle', ''))
    elif layout_name == 'Title and Content':
        return add_title_and_content_slide(prs, kwargs.get('title', ''), kwargs.get('content', ''))
    elif layout_name == 'Section Header':
        return add_section_header_slide(prs, kwargs.get('title', ''), kwargs.get('subtitle', ''))
    elif layout_name == 'Two Content':
        return add_two_content_slide(prs, kwargs.get('title', ''), kwargs.get('left_content', ''),
                                     kwargs.get('right_content', ''))
    elif layout_name == 'Comparison':
        return add_comparison_slide(prs, kwargs.get('title', ''), kwargs.get('left_title', ''),
                                    kwargs.get('left_content', ''),
                                    kwargs.get('right_title', ''), kwargs.get('right_content', ''))
    elif layout_name == 'Content with Caption':
        return add_content_with_caption_slide(prs, kwargs.get('title', ''), kwargs.get('content', ''),
                                              kwargs.get('caption', ''))
    elif layout_name == 'Picture with Caption':
        return add_picture_with_caption_slide(prs, kwargs.get('title', ''), kwargs.get('image_path', ''),
                                              kwargs.get('caption', ''))
    else:
        raise ValueError(f"Invalid layout name: {layout_name}")


def style_slide(slide, title_style=None, subtitle_style=None, content_style=None):
    """
    Áp dụng kiểu dáng cho slide.
    """
    if title_style and hasattr(slide.shapes, 'title') and slide.shapes.title:
        style_text(slide.shapes.title.text_frame, *title_style)

    if content_style:
        for shape in slide.placeholders:
            if shape.is_placeholder and shape.placeholder_format.idx != 0:
                if shape.has_text_frame:
                    style_text(shape.text_frame, *content_style)

    if subtitle_style:
        for shape in slide.placeholders:
            if shape.is_placeholder and shape.placeholder_format.idx == 1:
                if shape.has_text_frame:
                    style_text(shape.text_frame, *subtitle_style)


def set_slide_background(slide, bg_color=(255, 255, 255)):
    """
    Thay đổi màu nền cho slide.
    """
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(*bg_color)


def apply_style_to_all_slides(prs, title_style=None, subtitle_style=None, content_style=None):
    """
    Áp dụng kiểu dáng cho tất cả các slide.
    """
    for slide in prs.slides:
        style_slide(slide, title_style, subtitle_style, content_style)


def set_background_for_all_slides(prs, bg_color=(255, 255, 255)):
    """
    Thay đổi màu nền cho tất cả các slide.
    """
    for slide in prs.slides:
        set_slide_background(slide, bg_color)


def apply_global_styles(prs, template_name="light"):
    """
    Áp dụng style cho presentation dựa trên template có sẵn.
    Args:
        prs: Đối tượng Presentation
        template_name: Tên template (mặc định: "light")
    """
    TEMPLATES = {
        "light": {
            "title_style": ("Arial", 22, (31, 73, 125)),  # Navy Blue
            "subtitle_style": ("Arial", 16, (68, 114, 196)),  # Light Blue
            "content_style": ("Arial", 12, (0, 0, 0)),  # Black
            "bg_color": (255, 255, 255)  # White
        },
        "dark": {
            "title_style": ("Arial", 22, (255, 255, 255)),  # White
            "subtitle_style": ("Arial", 16, (189, 215, 238)),  # Light Blue
            "content_style": ("Arial", 12, (242, 242, 242)),  # Light Gray
            "bg_color": (44, 44, 44)  # Dark Gray
        },
        "monochrome": {
            "title_style": ("Tahoma", 22, (0, 0, 0)),  # Black
            "subtitle_style": ("Tahoma", 16, (64, 64, 64)),  # Dark Gray
            "content_style": ("Tahoma", 12, (89, 89, 89)),  # Medium Gray
            "bg_color": (242, 242, 242)  # Light Gray
        },
        "vibrant": {
            "title_style": ("Verdana", 22, (255, 89, 0)),  # Orange
            "subtitle_style": ("Verdana", 16, (0, 168, 133)),  # Turquoise
            "content_style": ("Verdana", 12, (64, 64, 64)),  # Dark Gray
            "bg_color": (255, 255, 240)  # Ivory
        },
        "elegant": {
            "title_style": ("Times New Roman", 22, (128, 0, 32)),  # Burgundy
            "subtitle_style": ("Times New Roman", 16, (112, 48, 48)),  # Dark Red
            "content_style": ("Roboto", 12, (64, 64, 64)),  # Dark Gray
            "bg_color": (245, 245, 245)  # Off White
        }
    }

    template = TEMPLATES.get(template_name, TEMPLATES["light"])

    apply_style_to_all_slides(
        prs,
        template["title_style"],
        template["subtitle_style"],
        template["content_style"]
    )
    set_background_for_all_slides(prs, template["bg_color"])

    return prs


def save_presentation(prs, output_path: str):
    """
    Lưu presentation.
    """
    try:
        prs.save(f'{SLIDE_FOLDER}/{output_path}')
    except Exception as e:
        raise IOError(f"Failed to save presentation: {str(e)}")


# Hàm chuyển đổi string thành dict
def convert_str_to_dict(s):
    """
    Chuyển đổi string thành dictionary.
    """
    s = s.split("\n")
    s = [line for line in s if line.strip()]
    res = {}
    for i in s:
        try:
            key, value = i.split(":", 1)
            res[key.strip()] = value.strip().strip('"')
        except ValueError:
            print(f"Warning: Skipping invalid line: {i}")
            continue
    return res
