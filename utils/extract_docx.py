from docx import Document

def extract_content_from_docx(file_path):
    """
    Extracts and returns the text content from a DOCX file.

    :param file_path: Path to the DOCX file
    :return: Extracted text content as a string
    """
    doc = Document(file_path)
    content = []

    for paragraph in doc.paragraphs:
        content.append(paragraph.text)

    return '\n'.join(content)