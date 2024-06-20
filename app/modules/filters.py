import cv2
import numpy as np

def apply_gaussian_blur(image_path, kernel_size):
    image = cv2.imread(image_path)
    kernel_size = (kernel_size, kernel_size)
    blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
    output_path = 'app/static/uploads/filtered_image.png'
    cv2.imwrite(output_path, blurred_image)
    return output_path

def apply_median_blur(image_path, kernel_size):
    image = cv2.imread(image_path)
    blurred_image = cv2.medianBlur(image, kernel_size)
    output_path = 'app/static/uploads/filtered_image.png'
    cv2.imwrite(output_path, blurred_image)
    return output_path

def apply_edge_detection(image_path, method='canny'):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if method == 'canny':
        edges = cv2.Canny(image, 100, 200)
    elif method == 'sobel':
        edges = cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=5)
    elif method == 'laplace':
        edges = cv2.Laplacian(image, cv2.CV_64F)
    output_path = f'app/static/uploads/filtered_image.png'
    cv2.imwrite(output_path, edges)
    return output_path
