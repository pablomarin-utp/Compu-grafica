import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Variable global para almacenar la imagen original
original_img = None

def open_image():
    global original_img
    route = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*")]
    )
    
    if not route:
        return
    
    original_img = Image.open(route)
    display_image(300)  # Tamaño inicial de 300x300

def display_image(size):
    if original_img:
        # Redimensiona la imagen según el tamaño del slider
        img_resized = original_img.resize((size, size))
        # Aplica el filtro de color según los checkboxes
        img_filtered = apply_color_filter(img_resized)
        img = ImageTk.PhotoImage(img_filtered)
        lbl.config(image=img)
        lbl.image = img

def on_slider_change(value):
    # Se ejecuta cada vez que el slider cambia
    size = int(value)
    display_image(size)

def on_channel_change():
    # Se ejecuta cada vez que se cambia un canal (checkbox)
    size = int(slider.get())
    display_image(size)

def apply_color_filter(img):
    if not (r_var.get() or g_var.get() or b_var.get()):
        # Si todos los canales están inactivos, mostrar en escala de grises
        return img.convert("L").convert("RGB")

    r, g, b = img.split()
    if not r_var.get():
        r = r.point(lambda i: 0)
    if not g_var.get():
        g = g.point(lambda i: 0)
    if not b_var.get():
        b = b.point(lambda i: 0)
    
    return Image.merge("RGB", (r, g, b))
root = tk.Tk()
root.title("Image Viewer with Slider")
root.geometry("600x600")

btn = tk.Button(root, text="Open Image", command=open_image)
btn.place(x=0, y=0)

lbl = tk.Label(root)
lbl.place(x=150, y=50)

# Slider para cambiar el tamaño
slider = tk.Scale(root, from_=1, to=500, orient=tk.HORIZONTAL, command=on_slider_change, label="Resize Image")
slider.set(300)  # Valor inicial
slider.place(x=150, y=400)

r_var = tk.BooleanVar(value=True)
g_var = tk.BooleanVar(value=True)
b_var = tk.BooleanVar(value=True)


r_checkbox = tk.Checkbutton(root, text="Show red", variable=r_var, command=on_channel_change)
g_checkbox = tk.Checkbutton(root, text="Show green", variable=g_var, command=on_channel_change)
b_checkbox = tk.Checkbutton(root, text="Show blue", variable=b_var, command=on_channel_change)

r_checkbox.place(x=150, y=450)
g_checkbox.place(x=250, y=450)
b_checkbox.place(x=350, y=450)

root.mainloop()
