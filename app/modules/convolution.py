import numpy as np
import cv2

def perform_convolution(image_path, kernel_size, sigma):
    # Cargar la imagen en escala de grises
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None, "No se pudo cargar la imagen."

    # Crear un kernel Gaussiano
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = np.outer(kernel, kernel.transpose())

    # Aplicar la convolución usando el kernel Gaussiano
    img_convolved = cv2.filter2D(img, -1, kernel)

    # Guardar la imagen resultante
    convolved_image_path = 'app/static/uploads/convolved_image.png'
    cv2.imwrite(convolved_image_path, img_convolved)

    return convolved_image_path, None
