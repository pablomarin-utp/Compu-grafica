import numpy as np

def layer(img, color):
    img_capa = np.zeros_like(img)
    img_capa[:,:,color] = img[:,:,color]
    return img_capa

