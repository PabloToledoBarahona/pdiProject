from flask import Blueprint, render_template, request, redirect, url_for
import os, time
from werkzeug.utils import secure_filename
from app.modules import histogram, read_image, segment_color, convert_bw, convolution
from app.modules.brightness import adjust_brightness
from app.modules.contrast import adjust_contrast

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

@image_controller.route('/convolve', methods=['GET', 'POST'])
def convolve_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            kernel_size = int(request.form.get('kernel_size', 5))
            sigma = float(request.form.get('sigma', 1.0))
            convolved_image_path, error = convolution.perform_convolution(file_path, kernel_size, sigma)
            if error:
                return error, 400
            timestamp = int(time.time())
            return render_template('convolve.html', original_image=filename, convolved_image='convolved_image.png', timestamp=timestamp)
    return render_template('convolve.html')



@image_controller.route('/adjust_brightness', methods=['GET', 'POST'])
def adjust_brightness_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            brightness_level = int(request.form.get('brightness', 0))
            modified_image_path, error = adjust_brightness(file_path, brightness_level)
            if error:
                return error, 400
            return render_template('adjust_brightness.html', original_image=filename, modified_image=modified_image_path)
    return render_template('adjust_brightness.html')


@image_controller.route('/adjust_contrast', methods=['GET', 'POST'])
def adjust_contrast_view():
    if request.method == 'POST':
        file = request.files.get('file')
        alpha = float(request.form.get('alpha', 1.0)) 
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            contrast_image_path, error = adjust_contrast(file_path, alpha)
            if error:
                return error, 400
            timestamp = int(time.time())
            return render_template('adjust_contrast.html', original_image=filename, contrast_image=contrast_image_path, timestamp=timestamp)
    return render_template('adjust_contrast.html')