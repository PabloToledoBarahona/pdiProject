import cv2
import numpy as np

def quantize_image(image_path, levels):
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."

    # Calcular el número de niveles de cuantización
    factor = 256 / (2**levels)

    # Cuantizar la imagen
    quantized_img = (img // factor) * factor

    output_path = 'app/static/uploads/quantized_image.png'
    cv2.imwrite(output_path, quantized_img)

    return output_path, None
