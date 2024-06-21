import cv2
import numpy as np
import os

def detect_edges(image_path, min_area):
    image = cv2.imread(image_path)
    if image is None:
        return None, "Imagen no encontrada."
        
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, filtered_contours, -1, (0, 255, 0), 3)

    output_path = os.path.join(os.path.dirname(image_path), "edge.jpg")
    cv2.imwrite(output_path, image_with_contours)

    return "edge.jpg", len(filtered_contours)
