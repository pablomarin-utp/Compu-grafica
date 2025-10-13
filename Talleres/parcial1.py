import numpy as np
import matplotlib.pyplot as plt


# Colores normalizados
black = np.array([0, 0, 0])
red = np.array([255, 0, 0]) / 255.0
green = np.array([0, 255, 0]) / 255.0
blue = np.array([0, 0, 255]) / 255.0
yellow = np.array([255, 255, 0]) / 255.0
magenta = np.array([255, 0, 255]) / 255.0
cyan = np.array([0, 255, 255]) / 255.0
#grises del 0.9 al 0.5
grays = []
for i in np.arange(0.9, 0.4, -0.1):
    grays.append(np.array([i, i, i]))

def ejercicio1(w=100, h=100):
    w_size = w // 10
    h_size = h // 10

    # Ahora matriz en floats, valores entre 0 y 1
    matrix = np.zeros((h, w, 3), dtype=float)


    #Poner las cosas en negro arriba y abajo
    matrix[:h_size, :, :] = black
    matrix[h-h_size:, :, :] = black

    #tres columnas de rojo, verde, azul
    matrix[h_size:h-h_size, :w_size] = red
    matrix[h_size:h-h_size, w_size:w_size*2] = green
    matrix[h_size:h-h_size, w_size*2:w_size*3] = blue

    #cuadrado amarillo de 3x2, magenta de 3x3 y cyan de 3x2
    matrix[h_size:h_size*4, w_size*3:w_size*5] = yellow
    matrix[h_size:h_size*4, w_size*5:w_size*8] = magenta
    matrix[h_size:h_size*4, w_size*8:] = cyan

    #el resto en gris
    for idx, gray in enumerate(grays):
        matrix[h_size*(idx+4):h_size*(idx+5), w_size*3:] = gray

    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')
    plt.show()


def ejercicio2(w=130, h=130):
    w_size = w // 13
    h_size = h // 13

    # Ahora matriz en floats, valores entre 0 y 1
    matrix = np.zeros((h, w, 3), dtype=float)


    #cuadrado cyan arriba a la izquierda, amarillo abajo a la izquierda y magenta abajo a la derecha
    matrix[h_size:h_size*5, w_size:w_size*5] = cyan
    matrix[h_size*8:h_size*12, w_size:w_size*5] = yellow
    matrix[h_size*8:h_size*12, w_size*8:w_size*12] = magenta

    # raya azul en el medio vertical y verde horizontal
    matrix[h_size*6:h_size*7, :] = green
    matrix[:, h_size*6:h_size*7] = blue

    #Cuadrado 3x3 rojo en el centro
    matrix[h_size*5:h_size*8, w_size*5:w_size*8] = red

    #cuadrado blanco en todo el centro 1x1
    matrix[h_size*6:h_size*7, w_size*6:w_size*7] = np.array([1.0, 1.0, 1.0])

    #cuadrado gris arriba a la derehca
    matrix[h_size:h_size*2, w_size*8:w_size*12] = grays[-1]
    matrix[h_size*4:h_size*5, w_size*8:w_size*12] = grays[-1]
    matrix[h_size*2:h_size*4, w_size*8:w_size*9] = grays[1]
    matrix[h_size*2:h_size*4, w_size*11:w_size*12] = grays[1]

    # Mostrar la matriz como una imagen
    plt.imshow(matrix)
    plt.axis('off')
    plt.show()

ejercicio1()
ejercicio2()