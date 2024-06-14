from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

image_controller = Blueprint('image_controller', __name__, template_folder='../templates')

UPLOAD_FOLDER = 'app/static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@image_controller.route('/')
def index():
    return render_template('index.html')

@image_controller.route('/upload', methods=['GET'])
def upload():
    return render_template('upload.html')

@image_controller.route('/handle_upload', methods=['POST'])
def handle_upload():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return redirect(url_for('image_controller.display_image', filename=filename))
    
    return redirect(url_for('image_controller.upload'))

@image_controller.route('/display_image/<filename>')
def display_image(filename):
    return render_template('display_image.html', filename=filename)
