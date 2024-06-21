import cv2

def add_images(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    if img1 is None or img2 is None:
        return None, "Failed to load one or both images."

    # Asegurarse de que ambas imágenes tienen el mismo tamaño
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    added_image = cv2.add(img1, img2)
    output_path = 'app/static/uploads/added_image.jpg'
    cv2.imwrite(output_path, added_image)
    return 'added_image.jpg', None

def subtract_images(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    if img1 is None or img2 is None:
        return None, "Failed to load one or both images."

    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    subtracted_image = cv2.subtract(img1, img2)
    output_path = 'app/static/uploads/subtracted_image.jpg'
    cv2.imwrite(output_path, subtracted_image)
    return 'subtracted_image.jpg', None
