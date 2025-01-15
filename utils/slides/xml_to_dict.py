import xml.etree.ElementTree as ET
from xml.dom import minidom


def xml_to_slides_dict(xml_content):
    try:
        # Parse XML string
        root = ET.fromstring(xml_content)
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return []

    slides = []

    # Lặp qua từng slide
    for slide in root.findall(".//slide"):
        slide_dict = {}

        # Lấy type (layout) của slide
        layout = slide.find("type")
        if layout is not None:
            slide_dict["layout"] = layout.text

        # Lấy các trường nội dung từ structure/field
        for field in slide.findall(".//field"):
            field_name = field.get("name")
            field_value = field.text
            slide_dict[field_name] = field_value

        slides.append(slide_dict)

    return slides


def slides_dict_to_xml(slides_list):
    """
    Chuyển đổi list của dictionary chứa thông tin slides thành XML string
    """

    def create_field_element(parent, name, value):
        """Tạo field element với xử lý đặc biệt cho nội dung có gạch đầu dòng"""
        field = ET.SubElement(parent, "field")
        field.set("name", name)
        if value:
            # Thêm khoảng trắng phía trước mỗi dòng để giữ indent
            lines = str(value).split("\n")
            processed_lines = []
            for line in lines:
                if line.strip().startswith("- "):
                    processed_lines.append("                " + line.strip())
                else:
                    processed_lines.append(line.strip())
            field.text = "\n".join(processed_lines)

    root = ET.Element("presentation")
    slides_element = ET.SubElement(root, "slides")

    for slide_dict in slides_list:
        slide = ET.SubElement(slides_element, "slide")

        if "layout" in slide_dict:
            type_elem = ET.SubElement(slide, "type")
            type_elem.text = slide_dict["layout"]

        structure = ET.SubElement(slide, "structure")

        for field_name, field_value in slide_dict.items():
            if field_name != "layout":
                create_field_element(structure, field_name, field_value)

    # Tạo XML string với định dạng đẹp
    rough_string = ET.tostring(root, encoding="unicode")
    reparsed = minidom.parseString(rough_string)

    # Xử lý đặc biệt để giữ nguyên indent cho bullet points
    xml_lines = reparsed.toprettyxml(indent="    ").split("\n")
    final_lines = []
    for line in xml_lines:
        if line.strip().startswith("- "):
            # Giữ nguyên dòng có gạch đầu dòng
            final_lines.append(line)
        else:
            # Loại bỏ khoảng trắng thừa cho các dòng khác
            final_lines.append(line.rstrip())

    return "\n".join(final_lines)
