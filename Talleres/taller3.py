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
     
    A = np.zeros((size,size), dtype=int)
    for row in range(3):
        for col in range(3):
            A[row*size//3:(row+1)*size//3, col*size//3:(col+1)*size//3] = matriz1[row,col]
    return A
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

if __name__ == "__main__":

    img = np.array(plt.imread('gatito.jpg'))

    # 1. Matriz con diseño
    diseno = matriz_diseno()
    mostrar(diseno)
    

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

    plt.show()


    
