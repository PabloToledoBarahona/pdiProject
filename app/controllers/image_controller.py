import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_controller = Blueprint('image_controller', __name__)

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@image_controller.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return redirect(url_for('image_controller.display_image', filename=filename))
    return render_template('upload.html')

@image_controller.route('/uploads/<filename>')
def display_image(filename):
    img_path = os.path.join(UPLOAD_FOLDER, filename)
    img = cv2.imread(img_path)
    y = detalles(img)
    return render_template('display_image.html', filename=filename)

def detalles(img):
    print("tam=", img.shape)
    print("max=", np.max(img))
    print("min=", np.min(img))
    x = img[:, :, 0]
    y = segmenta(x, 180)
    processed_image_path = 'app/static/uploads/processed_image.png'
    plt.imsave(processed_image_path, y, cmap='gray')
    return y

def segmenta(x, t):
    (F, C) = x.shape
    y = np.zeros((F, C))
    area = 0
    for i in range(F):
        for j in range(C):
            if x[i, j] > t:
                y[i, j] = 255
                area += 1
    print("area: ", area)
    return y
