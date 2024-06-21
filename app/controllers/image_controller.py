from flask import Blueprint, render_template, request, redirect, url_for
import os, time
from werkzeug.utils import secure_filename
from app.modules import histogram, read_image, segment_color, convert_bw, convolution, kernels
from app.modules.brightness import adjust_brightness
from app.modules.contrast import adjust_contrast
from app.modules.filters import apply_gaussian_blur, apply_median_blur, apply_edge_detection
from app.modules.transform_geometry import rotate_image
from app.modules.negative import make_negative
from app.modules.scale import scale_image
from app.modules.quantize import quantize_image
from app.modules.segment_k_clusters import segment_k_clusters
from app.modules.masks import apply_mask
from app.modules.edge_detection import detect_edges 
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

@image_controller.route('/filters', methods=['GET', 'POST'])
def filters_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            kernel_size = int(request.form.get('kernel_size', 5))
            filter_type = request.form.get('filter_type', 'gaussian')
            if filter_type == 'gaussian':
                output_path = apply_gaussian_blur(file_path, kernel_size)
            elif filter_type == 'median':
                output_path = apply_median_blur(file_path, kernel_size)
            elif filter_type in ['canny', 'sobel', 'laplace']:
                output_path = apply_edge_detection(file_path, filter_type)
            return render_template('filters.html', original_image=filename, filtered_image=output_path)
    return render_template('filters.html')


@image_controller.route('/transform_geometry', methods=['GET', 'POST'])
def transform_geometry_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            action = request.form['action']
            if action == 'rotate_90':
                transformed_path, error = rotate_image(file_path, 90)
            elif action == 'rotate_180':
                transformed_path, error = rotate_image(file_path, 180)
            elif action == 'rotate_270':
                transformed_path, error = rotate_image(file_path, 270)
            else:
                return "Acción no reconocida", 400
            if error:
                return error, 400
            return render_template('transform_geometry.html', transformed_image=os.path.basename(transformed_path))
    return render_template('transform_geometry.html')


@image_controller.route('/negative_image', methods=['GET', 'POST'])
def negative_image_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            negative_path, error = make_negative(file_path)
            if error:
                return error, 400
            return render_template('negative_image.html', negative_image=os.path.basename(negative_path))
    return render_template('negative_image.html')


@image_controller.route('/scale_image', methods=['GET', 'POST'])
def scale_image_view():
    if request.method == 'POST':
        file = request.files.get('file')
        scale_factor = float(request.form.get('scale_factor', 1.0))
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            scaled_path, error = scale_image(file_path, scale_factor)
            if error:
                return error, 400
            return render_template('scale_image.html', scaled_image=os.path.basename(scaled_path))
    return render_template('scale_image.html')


@image_controller.route('/quantize_image', methods=['GET', 'POST'])
def quantize_image_view():
    if request.method == 'POST':
        file = request.files.get('file')
        levels = int(request.form.get('levels', 4))
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            quantized_path, error = quantize_image(file_path, levels)
            if error:
                return error, 400
            return render_template('quantize_image.html', quantized_image=os.path.basename(quantized_path))
    return render_template('quantize_image.html')


@image_controller.route('/segment_k_clusters', methods=['GET', 'POST'])
def segment_k_clusters_view():
    if request.method == 'POST':
        file = request.files.get('file')
        clusters = int(request.form.get('clusters', 2))
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            segmented_path, error = segment_k_clusters(file_path, clusters)
            if error:
                return error, 400
            return render_template('segment_k_clusters.html', segmented_image=os.path.basename(segmented_path))
    return render_template('segment_k_clusters.html')


@image_controller.route('/masks', methods=['GET', 'POST'])
def masks_view():
    if request.method == 'POST':
        file = request.files.get('file')
        lower_color = request.form.get('lower_color').split(',')
        upper_color = request.form.get('upper_color').split(',')
        if file and lower_color and upper_color:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            masked_image_path, error = apply_mask(file_path, [int(x) for x in lower_color], [int(x) for x in upper_color])
            if error:
                return error, 400
            return render_template('masks.html', masked_image=os.path.basename(masked_image_path))
    return render_template('masks.html')


@image_controller.route('/apply_kernel', methods=['GET', 'POST'])
def apply_kernel():
    if request.method == 'POST':
        file = request.files.get('file')
        kernel_type = request.form.get('kernel_type')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            processed_image_path = kernels.apply_kernel(file_path, kernel_type)
            return render_template('kernels.html', original_image=filename, processed_image=os.path.basename(processed_image_path))
    return render_template('kernels.html')


@image_controller.route('/edge_detection', methods=['GET', 'POST'])
def edge_detection_view():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            min_area = int(request.form.get('min_area', 100))
            edge_image_path, count = detect_edges(file_path, min_area)
            return render_template('edge_detection.html', original_image=filename, edge_image=edge_image_path, count=count)
    return render_template('edge_detection.html')
