import cv2

def make_negative(image_path):
    # Cargar imagen
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."

    # Convertir a negativo
    negative = 255 - img

    # Guardar la imagen negativa
    output_path = 'app/static/uploads/negative.png'
    cv2.imwrite(output_path, negative)

    return output_path, None
