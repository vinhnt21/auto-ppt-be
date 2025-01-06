import PyPDF2
import os
from werkzeug.datastructures import FileStorage


class PdfHandler:
    def extract_text(self, file: FileStorage) -> str:
        try:
            # Save temporary file
            temp_path = os.path.join('uploads', 'temp', file.filename)
            file.save(temp_path)

            # Extract text
            text = ""
            with open(temp_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()

            # Clean up
            os.remove(temp_path)

            return text
        except Exception as e:
            raise Exception(f"Error processing PDF file: {str(e)}")
