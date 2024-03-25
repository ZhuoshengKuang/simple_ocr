from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
from pdf_ocr import pdf_to_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        base_name = os.path.splitext(filename)[0]
        text_file_name = f"{base_name}.txt"
        text_path = os.path.join(app.config['UPLOAD_FOLDER'], text_file_name)

        extracted_text = pdf_to_text(filepath)
        with open(text_path, 'w') as text_file:
            text_file.write(extracted_text)

        return send_file(text_path, as_attachment=True, download_name=f"{text_file_name}")


if __name__ == "__main__":
    app.run(debug=True)