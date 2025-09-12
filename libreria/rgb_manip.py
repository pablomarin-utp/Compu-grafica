import numpy as np


def layer(img, rgb=(1,1,1)):
    img_capa = np.zeros_like(img)
    
    for i in range(3):
        img_capa[:,:,i] = img[:,:,i] * rgb[i]  
        
    return img_capa

def invert(img):
    return 255 - img

def gray_scale(img):
    img = img / 255
    gray_img = (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3
    return gray_img


def combine_norezise(small, big, position=(0,0), factor=0.2):

    x, y = position
    h_s, w_s = small.shape[:2]
    x_start, y_start = max(0, x - w_s), max(0, y - h_s)

    new_image = big.copy()

    for row in range(h_s):
        for col in range(w_s):
            new_image[y_start + row, x_start + col] = small[row, col]*factor + big[y_start + row, x_start + col]*(1-factor)

    return new_image