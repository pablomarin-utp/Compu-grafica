import matplotlib.pyplot as plt
import numpy as np
import imgPro as im

img = plt.imread("gatito.jpg")

capa = im.layer(img, 0) 
plt.imshow(capa)


plt.axis("off")

plt.show()
