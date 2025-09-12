import matplotlib.pyplot as plt
import numpy as np

def image_from_path(path):
    img = plt.imread(path)
    return img

def show_image(img, title="Image", cmap=None):
    plt.imshow(img, cmap=cmap)
    plt.axis("off")
    plt.title(title)
    plt.show()


