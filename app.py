from flask import Flask, request, jsonify
from services.slides_service import SlideService
import env_config

app = Flask(__name__)

slide_service = SlideService()
app.config['MAX_CONTENT_LENGTH'] = env_config.MAX_CONTENT_LENGTH
app.config['UPLOAD_FOLDER'] = env_config.UPLOAD_FOLDER


@app.route('/api/slides/get-outline', methods=['POST'])
def get_outline():
    try:
        subject = request.form.get('subject')
        user_input = request.form.get('user_input')
        file = request.files.get('file')
        if not user_input and not file:
            return jsonify({'message': 'Phải nhập nội dung hoặc tải file'}), 400
        if file and file.filename.split('.')[-1].lower() not in ['docx', 'pdf'] and file:
            return jsonify({'message': 'File không hợp lệ'}), 400
        if not subject or subject not in ['math', 'civics']:
            return jsonify({'message': 'Subject không hợp lệ'}), 400
        result = slide_service.get_outline(file, user_input, subject)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/api/slides/get-content', methods=['POST'])
def get_content():
    try:
        data = request.get_json()
        outline = data.get('outline')
        subject = data.get('subject')
        content = data.get('content')
        if not outline or not subject:
            return jsonify({'message': 'Outline and subject are required'}), 400

        content = slide_service.get_slide_content(outline, subject, content)
        return jsonify({'content': content}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/api/slides/create-slide', methods=['POST'])
def create_slide():
    try:
        data = request.get_json()
        slide_content = data.get('slide_content')
        subject = data.get('subject')
        template_name = data.get('template_name')
        slide_file = slide_service.create_slide(slide_content, subject, template_name)
        return jsonify({'file': slide_file}), 200

    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
