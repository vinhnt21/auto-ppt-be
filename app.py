from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from utils.extract_docx import extract_content_from_docx
from utils.md2ppt import markdown_to_pptx
from ai.ai_models import *
from ai.ai_response import *
from datetime import datetime
from random import randint
from config import CODE
import os
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5MB
ALLOWED_EXTENSIONS = {"docx"}


def allowed_file(filename):
    try:
        return (
            "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
        )
    except Exception as e:
        logger.error(f"Error checking file extension: {str(e)}")
        return False


def ensure_directory_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except Exception as e:
        logger.error(f"Error creating directory {directory}: {str(e)}")
        raise


@app.route("/api/upload-docx", methods=["POST"])
def upload_docx():
    try:
        logger.info("Processing DOCX upload request")

        if "file" not in request.files:
            return jsonify({"error": "No file part"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400

        if not allowed_file(file.filename):
            return jsonify({"error": "Invalid file format"}), 400

        ensure_directory_exists(app.config["UPLOAD_FOLDER"])

        try:
            filename = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filename)

            docx_content = extract_content_from_docx(filename)
            slides_content = get_slide_content(docx_content)
            slides_content = slides_content.split("## ")
            slides_content = slides_content[1:]

            return jsonify({"slides_content": slides_content}), 200

        except Exception as e:
            logger.error(f"Error processing DOCX file: {str(e)}")
            return jsonify({"error": f"Error processing file: {str(e)}"}), 500

    except Exception as e:
        logger.error(f"Unexpected error in upload_docx: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/create-powerpoint", methods=["POST"])
def create_powerpoint():
    try:
        # slide_name = request.json.get("slide_name")
        slide_content = request.json.get("slides_content")
        slide_with_img = request.json.get("slide_with_img")

        if not slide_content:
            return jsonify({"error": "Slide content is required"}), 400
        if slide_with_img is None:
            return jsonify({"error": "Slide with image is required"}), 400

        ensure_directory_exists("slides")

        try:
            slide_content_str = "## ".join(slide_content)
            for i in range(len(slide_content)):
                slide_content[i] = "## " + slide_content[i]
                logger.info(f"Processing slide {i}")

                if i != 0 and i != len(slide_content) - 1:
                    img_url = (
                        get_img_description_for_slide_url(
                            slide_content[i], slide_content_str
                        )
                        if slide_with_img
                        else "./slides/_placeholder.png"
                    )
                    slide_content[i] += f"\n\n![img]({img_url})"

            md_content = "\n".join(slide_content)
            slide_name = get_slide_name(slide_content_str)
            # to avoid overwriting existing files add datetime and random number to the filename
            slide_name = f"{slide_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{randint(0, 9999)}"

            markdown_to_pptx(md_content, f"slides/{slide_name}.pptx")

            return jsonify(
                {
                    "link_to_download": f"/download/{slide_name}.pptx",
                    "slide_name": slide_name,
                }
            )

        except Exception as e:
            logger.error(f"Error creating PowerPoint: {str(e)}")
            return jsonify({"error": f"Error creating PowerPoint: {str(e)}"}), 500

    except Exception as e:
        logger.error(f"Unexpected error in create_powerpoint: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/api/download/<path:filename>", methods=["GET"])
def download_file(filename):
    try:
        return send_from_directory("slides", filename, as_attachment=True)
    except Exception as e:
        logger.error(f"Error downloading file {filename}: {str(e)}")
        return jsonify({"error": f"Error downloading file: {str(e)}"}), 500


@app.route("/api/check-code", methods=["POST"])
def check_code():
    try:
        code = request.json.get("code")
        if not code:
            return jsonify({"error": "Bắt buộc nhập code"}), 400
        if code == CODE:
            return jsonify({"success": "Code chính xác"}), 200
        return jsonify({"error": "Code không chính xác"}), 400
    except Exception as e:
        logger.error(f"Unexpected error in check_code: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500


