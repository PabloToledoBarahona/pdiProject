import cv2
import numpy as np

def apply_mask(image_path, lower_color, upper_color):
    # Cargar imagen
    image = cv2.imread(image_path)
    if image is None:
        return None, "No se pudo cargar la imagen."

    # Convertir a HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Crear la máscara
    mask = cv2.inRange(hsv_image, np.array(lower_color), np.array(upper_color))

    # Aplicar la máscara a la imagen
    result = cv2.bitwise_and(image, image, mask=mask)

    # Guardar la imagen resultante
    output_path = image_path.replace(".jpg", "_masked.jpg")
    cv2.imwrite(output_path, result)

    return output_path, None
