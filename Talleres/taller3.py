import numpy as np
import matplotlib.pyplot as plt

# ------------------- Funciones Auxiliares -------------------
def mostrar(img, titulo="Imagen", cmap=None):
    plt.imshow(img, cmap=cmap)
    plt.axis("off")
    plt.title(titulo)

# ------------------- 1. Matriz con diseño -------------------
def matriz_diseno(size=210):
     
    matriz1 = np.array([
        [[0,255,255], [255,255,255], [255,0,0]],      # Cian, Blanco, Rojo
        [[255,0,255], [128,128,128], [0,255,0]],      # Magenta, Gris, Verde
        [[255,255,0], [0,0,0],       [0,0,255]]       # Amarillo, Negro, Azul
    ], dtype=np.uint8)
     
    A = np.zeros((size,size,3), dtype=int)
    for row in range(3):
        for col in range(3):
            A[row*size//3:(row+1)*size//3, col*size//3:(col+1)*size//3] = matriz1[row,col]
   
   #mostrando con matplotlib

    plt.imshow(A)
    plt.axis("off")
    plt.show()


# ------------------- 2. Imagen desde matriz -------------------

def imagen_matriz(h=220, w=330):
    fila_h = h // 2
    col_w = w // 11  

    fila1 = [
        ([170,170,0], 1),    
        ([0,128,128], 2),    
        ([0,255,0], 2),    
        ([170,0,170], 2),   
        ([170,0,0], 2),     
        ([0,0,170], 2)      
    ]

    grises = [int(i*255/10) for i in range(1,11)]


    img = np.zeros((h, w, 3), dtype=np.uint8)

    start = 0
    for color, ancho_cols in fila1:
        end = start + ancho_cols*col_w
        img[:fila_h, start:end] = color
        start = end

    start = 0
    for g in reversed(grises):
        end = start + col_w
        img[fila_h:, start:end] = [g, g, g]
        start = end

    # Mostrar
    plt.imshow(img)
    plt.axis("off")
    plt.show()
    

# ------------------- 4-6. Capas R, G, B -------------------
def capa_roja(img):   r = img.copy(); r[:,:,1:]=0; return r
def capa_verde(img):  g = img.copy(); g[:,:,0]=0; g[:,:,2]=0; return g
def capa_azul(img):   b = img.copy(); b[:,:,:2]=0; return b

# ------------------- 7-9. Magenta, Cyan, Amarillo -------------------
def magenta(img): m = img.copy(); m[:,:,1]=0; return m
def cyan(img):    c = img.copy(); c[:,:,0]=0; return c
def amarillo(img):y = img.copy(); y[:,:,2]=0; return y


# -------------------- 10. Imagen de capas -------------------


def reconstruir_imagen(r, g, b):
    img_reconstruida = np.zeros_like(r)
    img_reconstruida[:,:,0] = r[:,:,0]
    img_reconstruida[:,:,1] = g[:,:,1]
    img_reconstruida[:,:,2] = b[:,:,2]
    return img_reconstruida

# ------------------- 11. Fusionar dos imágenes sin ecualizar -------------------
def fusionar_imagenes(img1, img2, alpha=0.5):
    f = img1*alpha + img2*(1-alpha)
    return f.astype(np.uint8)

# ------------------- 12. Fusionar dos imágenes ecualizadas -------------------
def ecualiza(img):
    img_eq = np.zeros_like(img)
    for c in range(3):
        plano = img[:,:,c]
        hist, _ = np.histogram(plano, bins=256, range=(0,255))
        cdf = hist.cumsum()
        cdf = (cdf - cdf.min())*255/(cdf.max()-cdf.min())
        img_eq[:,:,c] = cdf[plano]
    return img_eq.astype(np.uint8)

def fusionar_ecualizadas(img1, img2, alpha=0.5):
    eq1 = ecualiza(img1)
    eq2 = ecualiza(img2)
    f = eq1*alpha + eq2*(1-alpha)
    return f.astype(np.uint8)

# ------------------- 13. Escala de grises por Promedio -------------------
def gris_promedio(img):
    gris = (img[:,:,0] + img[:,:,1] + img[:,:,2]) // 3
    return gris.astype(np.uint8)

# ------------------- 14. Escala de grises por Luminosidad -------------------
def gris_luminosidad(img):
    gris = 0.299*img[:,:,0] + 0.587*img[:,:,1] + 0.114*img[:,:,2]
    return gris.astype(np.uint8)

# ------------------- 15. Escala de grises por Midgray -------------------
def gris_midgray(img):
    gris = (np.max(img, axis=2) + np.min(img, axis=2)) // 2
    return gris.astype(np.uint8)

# ------------------- Ejecución principal -------------------
if __name__ == "__main__":

    img = np.array(plt.imread('gatito.jpg'))
    img2 = np.array(plt.imread('gatito2.jpg'))  # Puede ser cualquier otra imagen rgb igual tamaño

    # 1. Matriz con diseño
    matriz_diseno()
    
    # 2.
    imagen_matriz()

    # 4. Capa roja
    img_roja = capa_roja(img)
    plt.figure()
    mostrar(img_roja, "Capa Roja")

    # 5. Capa verde
    img_verde = capa_verde(img)
    plt.figure()
    mostrar(img_verde, "Capa Verde")

    # 6. Capa azul
    img_azul = capa_azul(img)
    plt.figure()
    mostrar(img_azul, "Capa Azul")

    # 7. Magenta
    img_magenta = magenta(img)
    plt.figure()
    mostrar(img_magenta, "Magenta")

    # 8. Cyan
    img_cyan = cyan(img)
    plt.figure()
    mostrar(img_cyan, "Cyan")

    # 9. Amarillo
    img_amarillo = amarillo(img)
    plt.figure()
    mostrar(img_amarillo, "Amarillo")

    # 11. Fusión de dos imágenes sin ecualizar
    fusion_simple = fusionar_imagenes(img, img2)
    plt.figure()
    mostrar(fusion_simple, "Fusión sin Ecualizar")

    # 12. Fusión de dos imágenes ecualizadas
    fusion_eq = fusionar_ecualizadas(img, img2)
    plt.figure()
    mostrar(fusion_eq, "Fusión Ecualizada")

    # 13. Escala de grises promedio
    gris_prom = gris_promedio(img)
    plt.figure()
    mostrar(gris_prom, "Grises Promedio", cmap='gray')

    # 14. Escala de grises luminosidad
    gris_lum = gris_luminosidad(img)
    plt.figure()
    mostrar(gris_lum, "Grises Luminosidad", cmap='gray')

    # 15. Escala de grises midgray
    gris_mid = gris_midgray(img)
    plt.figure()
    mostrar(gris_mid, "Grises Midgray", cmap='gray')

    plt.show()
