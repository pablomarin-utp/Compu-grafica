import numpy as np
import matplotlib.pyplot as plt 

def color_matrix(w=100, h=100):
    w_size = w // 10
    h_size = h // 10

    # Ahora matriz en floats, valores entre 0 y 1
    matrix = np.zeros((h, w, 3), dtype=float)
    
    # Bordes blancos
    matrix[h_size:h-h_size, w_size:2*w_size] = [1.0, 1.0, 1.0] 
    matrix[h_size:h-h_size, w-2*w_size:w-w_size] = [1.0, 1.0, 1.0]

    # Colores normalizados
    colors = np.array([
        [255, 0, 0],    
        [0, 255, 0],    
        [0, 0, 255],    
        [128, 128, 128],
        [128, 128, 128],
        [0, 255, 255],  
        [255, 0, 255],  
        [255, 255, 0]   
    ]) / 255.0   # ← aquí los pasamos a [0,1]

    for i, color in enumerate(colors):
        matrix[h_size + h_size*i:h_size + h_size*(i+1), w_size*2:w-2*w_size] = color

    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')
    plt.show()

color_matrix(100, 100)
