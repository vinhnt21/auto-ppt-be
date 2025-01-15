from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import send_from_directory

from services.slides_service import SlideService
import env_config

app = Flask(__name__)
CORS(app)
slide_service = SlideService()
app.config["MAX_CONTENT_LENGTH"] = env_config.MAX_CONTENT_LENGTH
app.config["UPLOAD_FOLDER"] = env_config.UPLOAD_FOLDER
app.config["SLIDE_FOLDER"] = env_config.SLIDE_FOLDER


@app.route("/api/slides/get-outline", methods=["POST"])
def get_outline():
    try:
        user_input = request.form.get("user_input")
        file = request.files.get("file")
        if not user_input and not file:
            return jsonify({"message": "Phải nhập nội dung hoặc tải file"}), 400
        if (
            file
            and file.filename.split(".")[-1].lower() not in ["docx", "pdf"]
            and file
        ):
            return jsonify({"message": "File không hợp lệ"}), 400
        result = slide_service.get_outline(file, user_input)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/api/slides/get-content", methods=["POST"])
def get_content():
    try:
        data = request.get_json()
        outline = data.get("outline")
        content = data.get("content")

        result = slide_service.get_slide_content(outline, content)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/api/slides/create-slide", methods=["POST"])
def create_slide():
    try:
        data = request.get_json()
        slides = data.get("slides")
        template_name = data.get("template_name")
        result = slide_service.create_slide(slides, template_name)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"message": str(e)}), 400


@app.route("/api/slides/download/<file_name>", methods=["GET"])
def download_file(file_name):
    try:
        return send_from_directory(
            app.config["SLIDE_FOLDER"],
            file_name,
            as_attachment=True,
            environ=request.environ,
        )
    except Exception as e:
        return jsonify({"message": str(e)}), 400


# if __name__ == "__main__":
#     app.run(debug=True)
