from dotenv import load_dotenv
import os

load_dotenv()

# AI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# App Configuration
CODE = os.getenv("CODE")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
SLIDE_FOLDER = os.getenv("SLIDE_FOLDER")
MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH", 10 * 1024 * 1024))