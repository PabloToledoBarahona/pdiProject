import cv2

def adjust_brightness(image_path, brightness=0):
    # Cargar la imagen
    image = cv2.imread(image_path)
    if image is None:
        return None, "No se pudo cargar la imagen."

    # Ajustar el brillo
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, brightness)
    final_hsv = cv2.merge((h, s, v))
    image_bright = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

    # Guardar la imagen resultante
    modified_image_path = 'app/static/uploads/modified_image.png'
    cv2.imwrite(modified_image_path, image_bright)

    return modified_image_path, None
