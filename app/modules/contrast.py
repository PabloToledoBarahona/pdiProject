import cv2
import numpy as np

def adjust_contrast(image_path, alpha):
    # Carga la imagen
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."
    
    # Ajusta el contraste de la imagen
    # `alpha` es el factor de contraste, si es > 1 aumentará el contraste
    # si es < 1 disminuirá el contraste.
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=0)
    
    # Guardar la imagen resultante
    result_image_path = 'app/static/uploads/contrast_adjusted.png'
    cv2.imwrite(result_image_path, adjusted)
    
    return result_image_path, None
