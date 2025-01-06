from docx import Document
import os
from werkzeug.datastructures import FileStorage
from env_config import UPLOAD_FOLDER


class DocxHandler:
    def extract_text(self, file: FileStorage) -> str:
        try:
            # Save temporary file
            temp_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(temp_path)

            # Extract text
            doc = Document(temp_path)
            text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])

            # Clean up
            os.remove(temp_path)

            return text
        except Exception as e:
            raise Exception(f"Error processing DOCX file: {str(e)}")
