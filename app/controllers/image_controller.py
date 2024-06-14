from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from app.modules import read_image, segment_color, convert_bw, brightness, contrast, negative, scale, histogram, quantization, reshape, k_clusters, geometric_transform, filters, edge_detection, object_detection, convolution, fourier, morphology, image_arithmetic

image_controller = Blueprint('image_controller', __name__, template_folder='../templates')

UPLOAD_FOLDER = 'app/static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@image_controller.route('/')
def index():
    return render_template('index.html')

@image_controller.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
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
    return render_template('upload.html')

@image_controller.route('/display_image/<filename>')
def display_image(filename):
    return render_template('display_image.html', filename=filename)

# Agregar rutas adicionales para cada funcionalidad, utilizando los módulos correspondientes.
# Ejemplo:
@image_controller.route('/read_image/<filename>')
def read_image_func(filename):
    return read_image.display_image_info(filename)

# Y así sucesivamente para las demás funcionalidades.
