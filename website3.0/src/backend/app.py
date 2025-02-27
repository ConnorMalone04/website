from flask import Flask, request, send_file
from flask_cors import CORS
import os
import subprocess

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/app', methods=['GET'])
def test():
    return "CORS test successful"

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded.", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected.", 400

    # Save the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # call python processes
    try:
        result = subprocess.run(
            ['python3', 'ascii-gen.py', file_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            return f"Error processing file: {result.stderr}", 500

        output_path = result.stdout.strip()

        return send_file(output_path, as_attachment=True, download_name='output.txt')

    except Exception as e:
        return f"Error: {str(e)}", 500

    finally:
        # clean up the uploaded file and the generated text file
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(output_path):
            os.remove(output_path)

if __name__ == '__main__':
    app.run(debug=True)