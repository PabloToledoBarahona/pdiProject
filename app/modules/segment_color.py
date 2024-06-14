import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib

# Usar el backend 'Agg' para evitar problemas de GUI
matplotlib.use('Agg')

def segment_by_color(image_path, color_channel, threshold):
    print(f"Cargando imagen desde: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        return None, "Error: No se ha encontrado la imagen."

    # Convertir la imagen de BGR a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Seleccionar el canal de color
    if color_channel == 'red':
        channel = img_rgb[:, :, 0]
    elif color_channel == 'green':
        channel = img_rgb[:, :, 1]
    elif color_channel == 'blue':
        channel = img_rgb[:, :, 2]
    else:
        return None, "Error: Canal de color no válido."

    # Segmentar la imagen
    (F, C) = channel.shape
    segmented = np.zeros((F, C))
    for i in range(F):
        for j in range(C):
            if channel[i, j] > threshold:
                segmented[i, j] = 255

    # Guardar la imagen segmentada
    segmented_image_path = f'app/static/uploads/segmented_{color_channel}.png'
    plt.imsave(segmented_image_path, segmented, cmap='gray')

    return segmented_image_path, None
