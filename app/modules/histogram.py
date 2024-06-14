import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib

# Usar el backend 'Agg' para evitar problemas de GUI
matplotlib.use('Agg')

def compute_histogram(image_path):
    print(f"Cargando imagen desde: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        return None, None, "Error: No se ha encontrado la imagen."

    # Convertir la imagen de BGR a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Separar los canales de color
    R = img_rgb[:, :, 0]
    G = img_rgb[:, :, 1]
    B = img_rgb[:, :, 2]

    # Preparar los datos para el histograma
    r = R.flatten()
    g = G.flatten()
    b = B.flatten()

    # Ecualizar la imagen
    img_eq = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2YCrCb)
    img_eq[:, :, 0] = cv2.equalizeHist(img_eq[:, :, 0])
    img_eq = cv2.cvtColor(img_eq, cv2.COLOR_YCrCb2RGB)

    # Separar los canales de color de la imagen ecualizada
    R_eq = img_eq[:, :, 0]
    G_eq = img_eq[:, :, 1]
    B_eq = img_eq[:, :, 2]

    # Preparar los datos para el histograma de la imagen ecualizada
    r_eq = R_eq.flatten()
    g_eq = G_eq.flatten()
    b_eq = B_eq.flatten()

    # Crear el histograma
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.hist(r, bins=256, range=(0, 256), histtype='step', color='red')
    plt.hist(g, bins=256, range=(0, 256), histtype='step', color='green')
    plt.hist(b, bins=256, range=(0, 256), histtype='step', color='blue')
    plt.title('Histograma Original')
    plt.xlabel('Valor de píxel')
    plt.ylabel('Frecuencia')
    plt.legend(['Rojo', 'Verde', 'Azul'])
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.hist(r_eq, bins=256, range=(0, 256), histtype='step', color='red')
    plt.hist(g_eq, bins=256, range=(0, 256), histtype='step', color='green')
    plt.hist(b_eq, bins=256, range=(0, 256), histtype='step', color='blue')
    plt.title('Histograma Ecualizado')
    plt.xlabel('Valor de píxel')
    plt.ylabel('Frecuencia')
    plt.legend(['Rojo', 'Verde', 'Azul'])
    plt.grid(True)

    # Guardar el histograma como imagen temporal
    histogram_path = 'app/static/uploads/histogram_comparison.png'
    plt.savefig(histogram_path)
    plt.close()

    # Guardar la imagen ecualizada
    eq_image_path = 'app/static/uploads/equalized_image.png'
    cv2.imwrite(eq_image_path, cv2.cvtColor(img_eq, cv2.COLOR_RGB2BGR))

    return histogram_path, eq_image_path, None
