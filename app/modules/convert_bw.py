import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib

# Usar el backend 'Agg' para evitar problemas de GUI
matplotlib.use('Agg')

def convert_to_bw(image_path, r_weight, g_weight, b_weight):
    print(f"Cargando imagen desde: {image_path}")
    img = cv2.imread(image_path)
    if img is None:
        return None, "Error: No se ha encontrado la imagen."

    # Convertir la imagen de BGR a RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Separar los canales de color
    R = img_rgb[:, :, 0].astype(float)
    G = img_rgb[:, :, 1].astype(float)
    B = img_rgb[:, :, 2].astype(float)

    # Convertir a blanco y negro usando los pesos proporcionados
    bw_image = r_weight * R + g_weight * G + b_weight * B
    bw_image = np.clip(bw_image, 0, 255).astype(np.uint8)

    # Guardar la imagen en blanco y negro
    bw_image_path = 'app/static/uploads/bw_image.png'
    plt.imsave(bw_image_path, bw_image, cmap='gray')

    return bw_image_path, None
