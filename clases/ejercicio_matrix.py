import numpy as np
import matplotlib.pyplot as plt 


def color_matrix(w=100, h=100):
    """
    Crea una matriz de colores y la muestra como una imagen.
    
    Parámetros:
    w (int): Ancho de la matriz.
    h (int): Alto de la matriz.
    """

    w_size = w // 10
    h_size = h // 10

    # Crear una matriz de ceros con 3 canales (RGB)
    matrix = np.zeros((h, w, 3), dtype=np.uint8)
    
    

    matrix[h_size:h-h_size, w_size:2*w_size] = [255, 255, 255] 
    matrix[h_size:h-h_size, w-2*w_size:w-w_size] = [255, 255, 255]

    #rojo, verde, azul, gris, gris, cian, magenta, amarillo
    colors = [
        [255, 0, 0],    # Rojo
        [0, 255, 0],    # Verde
        [0, 0, 255],    # Azul
        [128, 128, 128],# Gris
        [128, 128, 128],# Gris 
        [0, 255, 255],  # Cian
        [255, 0, 255],  # Magenta
        [255, 255, 0]   # Amarillo
    ]

    for i, color in enumerate(colors):
        matrix[h_size + h_size*i:h_size + h_size*(i+1), w_size*2:w-2*w_size] = color

    

    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')  # Ocultar los ejes
    plt.show()

color_matrix(100, 100)