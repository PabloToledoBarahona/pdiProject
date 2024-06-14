import cv2

def get_image_info(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None, "Error: Image not found."
    
    # Obtener las dimensiones de la imagen
    img_shape = img.shape

    return img_shape, None
