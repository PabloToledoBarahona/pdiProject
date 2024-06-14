import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use('Agg')

def compute_histogram(image_path):
    print(f"Cargando imagen desde: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        return None, "Error: No se ha encontrado la imagen."

    # Convertir la imagen de BGR a RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Separar los canales de color
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    # Preparar los datos para el histograma
    r = R
    (N, M) = r.shape
    r.shape = (N * M)

    g = G
    (N, M) = g.shape
    g.shape = (N * M)

    b = B
    (N, M) = b.shape
    b.shape = (N * M)

    # Crear el histograma
    plt.figure()
    plt.hist(r, bins=256, range=(0, 256), histtype='step', color='red')
    plt.hist(g, bins=256, range=(0, 256), histtype='step', color='green')
    plt.hist(b, bins=256, range=(0, 256), histtype='step', color='blue')
    plt.title('Histograma')
    plt.xlabel('Valor de píxel')
    plt.ylabel('Frecuencia')
    plt.legend(['Rojo', 'Verde', 'Azul'])
    plt.grid(True)

    # Guardar el histograma como imagen temporal
    histogram_path = 'app/static/uploads/histogram.png'
    plt.savefig(histogram_path)
    plt.close()

    return histogram_path, None
