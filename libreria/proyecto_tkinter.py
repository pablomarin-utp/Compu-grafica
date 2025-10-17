import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import imgPro as ip   # <-- importa tus funciones

# === Variables globales ===
img_original = None
img_procesada = None
img2 = None  # para fusión

def abrir_imagen():
    global img_original,img2
    ruta = filedialog.askopenfilename(
        title="Selecciona una imagen",
        filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"), ("Todos", "*.*")]
    )
    if not ruta:
        return
    
    img_original = Image.open(ruta).resize((400, 300))
    mostrar_imagen(img_original)
    """
    elif num == 1:
        img_original = Image.open(ruta).resize((400, 300))
        mostrar_imagen(img_original)
    
    elif num == 1:
        img2 = Image.open(ruta).resize((400, 300))
        mostrar_imagen(img2)
    """
        

def mostrar_imagen(img):
    foto = ImageTk.PhotoImage(img)
    lbl.config(image=foto)
    lbl.image = foto  


def guardar_imagen():
    global img_procesada
    if img_procesada is None:
        messagebox.showwarning("Atención", "No hay imagen procesada para guardar.")
        return
    ruta = filedialog.asksaveasfilename(defaultextension=".png",
                                        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
    if ruta:
        img_procesada.save(ruta)
        messagebox.showinfo("Guardar", "Imagen guardada correctamente.")


# === Aplicaciones de tus funciones ===

def aplicar_brillo_btn(value):
    global img_original
    if img_original is None:
        return
    try:
        val = float(value)
    except ValueError:
        val = 0.0
    img_np = np.array(img_original, dtype=np.float32)
    img_np = ip.ajustar_brillo(img_np, val)
    img_pil = Image.fromarray(img_np.astype(np.uint8))
    mostrar_imagen(img_pil)


"""def aplicar_brillo_canal(value):
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return
    try:
        val = float(value)
    except ValueError:
        val = 0.0
    img_np = np.array(img_original, dtype=np.float32)
    img_np = ip.ajustar_brillo_canal(img_np, val)
    img_procesada = Image.fromarray(img_np)
    mostrar_imagen(img_procesada)

"""
def aplicar_brillo_canal(canal, value):
    """Ajusta el brillo de los canales R, G y B según los sliders."""
    global img_original, img_procesada, valores_rgb
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    # Actualizar el valor del canal correspondiente
    valores_rgb[canal] = float(value) * 100  # escala -1..1 a -100..100

    # Aplicar el brillo por canal
    img_np = np.array(img_original)
    resultado = ip.ajustar_brillo_canal(img_np, valores_rgb)
    img_procesada = Image.fromarray(resultado)

    mostrar_imagen(img_procesada)
    """
def aplicar_log():
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    img_np = np.array(img_original)
    resultado = ip.contraste_logaritmico(img_np, c=1.2)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada, lbl_resultado)

def aplicar_exp():
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    img_np = np.array(img_original)
    resultado = ip.contraste_exponencial(img_np, gamma=0.8)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada, lbl_resultado)

def aplicar_crop():
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    x1, y1, x2, y2 = 100, 100, 400, 400
    img_np = np.array(img_original)
    resultado = ip.recortar_imagen(img_np, x1, y1, x2, y2)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada, lbl_resultado)

def aplicar_fusion():
    global img_original, img2, img_procesada
    if img_original is None or img2 is None:
        messagebox.showwarning("Atención", "Debes abrir las dos imágenes primero.")
        return

    img1_np = np.array(img_original.resize((400, 400)))
    img2_np = np.array(img2.resize((400, 400)))
    resultado = ip.fusionar_imagenes(img1_np, img2_np, alpha=0.5)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada, lbl_resultado)

"""
# === Interfaz Tkinter ===
root = tk.Tk()
root.title("Procesamiento de Imágenes")
root.geometry("1000x600")

res_img = root.resizable(False,False)
boton = tk.Button(root, text= "Abrir imagen",command=abrir_imagen)
boton.place(x=10,y=10)

lbl = tk.Label(root)
lbl.place(x=40,y=40)

slider_brillo = tk.Scale(root, from_=-1, to= 1, resolution= 0.01, orient= tk.HORIZONTAL, length= 220, command= aplicar_brillo_btn)

slider_brillo.set(0.0)
slider_brillo.place(x = 420, y = 5)


# Botones principales


root.mainloop()
