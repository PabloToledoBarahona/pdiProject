import cv2
import numpy as np

def apply_morphology(image_path, morph_type, iterations):
    image = cv2.imread(image_path)
    if image is None:
        return None, "Failed to load image."
    kernel = np.ones((5, 5), np.uint8)
    
    if morph_type == "dilation":
        result = cv2.dilate(image, kernel, iterations=iterations)
    elif morph_type == "erosion":
        result = cv2.erode(image, kernel, iterations=iterations)

    output_path = 'app/static/uploads/morphology.jpg'
    cv2.imwrite(output_path, result)

    return 'morphology.jpg'

