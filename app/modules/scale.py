import cv2

def scale_image(image_path, scale_factor):
    # Cargar imagen
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."

    # Calcular nuevas dimensiones
    new_width = int(img.shape[1] * scale_factor)
    new_height = int(img.shape[0] * scale_factor)

    # Escalar la imagen
    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Guardar la imagen escalada
    output_path = 'app/static/uploads/scaled_image.png'
    cv2.imwrite(output_path, resized_img)

    return output_path, None
