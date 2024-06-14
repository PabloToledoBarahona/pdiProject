from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from app.modules import histogram, read_image, segment_color, convert_bw

image_controller = Blueprint('image_controller', __name__, template_folder='../templates')

UPLOAD_FOLDER = 'app/static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@image_controller.route('/')
def index():
    image_files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', image_files=image_files)

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

@image_controller.route('/histogram', methods=['GET', 'POST'])
def show_histogram():
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
            histogram_path, eq_image_path, error = histogram.compute_histogram(file_path)
            if error:
                return error, 400
            return render_template('histogram.html', histogram_path=os.path.basename(histogram_path), eq_image_path=os.path.basename(eq_image_path), filename=filename)
    return render_template('histogram.html')

@image_controller.route('/read_image', methods=['GET', 'POST'])
def read_image_view():
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
            img_shape, error = read_image.get_image_info(file_path)
            if error:
                return error, 400
            return render_template('read_image.html', img_shape=img_shape, filename=filename)
    return render_template('read_image.html')

@image_controller.route('/segment_color', methods=['GET', 'POST'])
def segment_color_view():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        color_channel = request.form.get('color_channel')
        threshold = int(request.form.get('threshold', 128))
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            segmented_image_path, error = segment_color.segment_by_color(file_path, color_channel, threshold)
            if error:
                return error, 400
            return render_template('segment_color.html', segmented_image_path=os.path.basename(segmented_image_path), filename=filename)
    return render_template('segment_color.html')

@image_controller.route('/convert_bw', methods=['GET', 'POST'])
def convert_bw_view():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        r_weight = float(request.form.get('r_weight', 0.33))
        g_weight = float(request.form.get('g_weight', 0.33))
        b_weight = float(request.form.get('b_weight', 0.33))
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            bw_image_path, error = convert_bw.convert_to_bw(file_path, r_weight, g_weight, b_weight)
            if error:
                return error, 400
            return render_template('convert_bw.html', bw_image_path=os.path.basename(bw_image_path), filename=filename)
    return render_template('convert_bw.html')
