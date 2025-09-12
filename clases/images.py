import numpy as np
import matplotlib.pyplot as plt 

img = np.array(plt.imread('gatito.jpg'))

# Copias de la imagen original
imgR = img.copy()
imgG = img.copy()
imgB = img.copy()
imgMagenta = img.copy()
imgYellow = img.copy()
imgOrange = img.copy()
imgCyan = img.copy()

# Apagar los canales que no correspondan
imgR[:,:,1] = 0   # quita el verde
imgR[:,:,2] = 0   # quita el azul

imgG[:,:,0] = 0   # quita el rojo
imgG[:,:,2] = 0   # quita el azul

imgB[:,:,0] = 0   # quita el rojo
imgB[:,:,1] = 0   # quita el verde

imgMagenta[:,:,0] = 255   # quita el verde
imgMagenta[:,:,2] = 255   # quita el azul

imgYellow[:,:,0] = 255   # quita el rojo
imgYellow[:,:,1] = 255   # quita el azul

imgOrange[:,:,2] = 0
imgOrange[:,:,1] = (imgOrange[:,:,1] * 0.5).astype(np.uint8)

imgCyan[:,:,2] = 255   # quita el rojo
imgCyan[:,:,1] = 255   # quita el verde

print(img.shape)

plots = [img, imgR, imgG, imgB, imgMagenta, imgYellow, imgOrange, imgCyan]
colors = ['Original', 'Red', 'Green', 'Blue', 'Magenta', 'Yellow', 'Orange', 'Cyan']
for i, plot in enumerate(plots):
    plt.subplot(3,3,i+1)
    plt.imshow(plot)
    plt.axis('off')
    plt.title(colors[i])

plt.show()
