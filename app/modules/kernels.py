import numpy as np
import cv2

def apply_kernel(image_path, kernel_type):
    img = cv2.imread(image_path)
    kernels = {
        'average': np.ones((5,5), np.float32) / 25,
        'edge_detection1': np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]),
        'edge_detection2': np.array([[-1,8,-1], [-1,4,-1], [-1,4,-1], [-1,8,-1]])
    }
    kernel = kernels.get(kernel_type, kernels['average'])
    processed_image = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    output_path = f'app/static/uploads/{kernel_type}_processed.png'
    cv2.imwrite(output_path, processed_image)
    return output_path
