import cv2
import numpy as np

def detect_objects(image_path, min_area):
    image = cv2.imread(image_path)
    if image is None:
        return None, "No se pudo cargar la imagen."
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Aplicar operaciones morfológicas
    kernel = np.ones((3,3), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    objects_data = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > min_area:
            perimeter = cv2.arcLength(cnt, True)
            M = cv2.moments(cnt)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
            else:
                cx, cy = 0, 0
            objects_data.append((area, perimeter, cx, cy))
            cv2.drawContours(image, [cnt], -1, (0, 255, 0), 3)
            cv2.circle(image, (cx, cy), 5, (0, 0, 255), -1)

    output_path = 'app/static/uploads/objects_detected.jpg'
    cv2.imwrite(output_path, image)

    return output_path, objects_data
