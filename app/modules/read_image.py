import cv2
from matplotlib import pyplot as plt

def display_image_info(filename):
    img = cv2.imread(f'app/static/uploads/{filename}')
    img_info = {
        "shape": img.shape,
        "max_value": img.max(),
        "min_value": img.min()
    }
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()
    return img_info
