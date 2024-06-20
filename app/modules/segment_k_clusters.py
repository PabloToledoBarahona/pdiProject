import cv2
import numpy as np

def segment_k_clusters(image_path, clusters):
    img = cv2.imread(image_path)
    if img is None:
        return None, "No se pudo cargar la imagen."

    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label, center = cv2.kmeans(Z, clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    center = np.uint8(center)
    res = center[label.flatten()]
    result_image = res.reshape((img.shape))

    output_path = f'app/static/uploads/segmented_k{clusters}.png'
    cv2.imwrite(output_path, result_image)

    return output_path, None
