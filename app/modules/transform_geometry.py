import cv2

def rotate_image(image_path, angle):
    # Cargar imagen
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."

    # Obtener dimensiones de la imagen
    (h, w) = img.shape[:2]
    # Punto de centro para la rotación
    center = (w // 2, h // 2)

    # Matriz de rotación
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Rotar la imagen
    rotated = cv2.warpAffine(img, M, (w, h))

    # Guardar la imagen rotada
    output_path = f'app/static/uploads/rotated_{angle}.png'
    cv2.imwrite(output_path, rotated)

    return output_path, None
