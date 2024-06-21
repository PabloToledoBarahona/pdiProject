import numpy as np
import cv2
from numpy.fft import fft2, fftshift, ifft2

def apply_fourier_transform(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return None, "Failed to load image."

    # Applying Fourier Transform
    f_transform = fft2(image)
    f_shift = fftshift(f_transform)
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))

    # Converting back to uint8 image
    magnitude_image = np.asarray(magnitude_spectrum, dtype=np.uint8)

    # Inverse Fourier Transform
    f_ishift = fftshift(f_transform)
    img_back = ifft2(f_ishift)
    img_back = np.abs(img_back)

    # Saving the results with specific names
    output_path_spectrum = 'app/static/uploads/fourier_spectrum.jpg'
    output_path_inverse = 'app/static/uploads/fourier_inverse.jpg'
    cv2.imwrite(output_path_spectrum, magnitude_image)
    cv2.imwrite(output_path_inverse, np.asarray(img_back, dtype=np.uint8))

    return output_path_spectrum, output_path_inverse
