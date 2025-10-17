import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import imgPro as ip   # <-- importa tus funciones

# === Variables globales ===
img_original = None
img_procesada = None
img2 = None  # para fusión
widgets_dinamicos = []  # para guardar y eliminar widgets temporales
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
def aplicar_log():
    global img_original, img_procesada
    if img_original is None:
        return
    img_np = np.array(img_original)
    resultado = ip.contraste_logaritmico(img_np, c=1)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada)

def aplicar_exp():
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    img_np = np.array(img_original)
    img_np = ip.contraste_exponencial(img_np, gamma=1)
    img_procesada = Image.fromarray(img_np)
    mostrar_imagen(img_procesada)


def limpiar_widgets():
    """Elimina los widgets temporales (sliders, entries, etc.)"""
    global widgets_dinamicos
    for w in widgets_dinamicos:
        w.destroy()
    widgets_dinamicos = []

def modo_recorte():
    """Activa el modo recorte: muestra las cajas para ingresar coordenadas"""
    limpiar_widgets()  # limpia sliders, entradas previas, etc.
    global widgets_dinamicos

    tk.Label(root, text="x1:").place(x=420, y=20)
    x1_entry = tk.Entry(root, width=5)
    x1_entry.place(x=450, y=20)

    tk.Label(root, text="y1:").place(x=500, y=20)
    y1_entry = tk.Entry(root, width=5)
    y1_entry.place(x=530, y=20)

    tk.Label(root, text="x2:").place(x=420, y=50)
    x2_entry = tk.Entry(root, width=5)
    x2_entry.place(x=450, y=50)

    tk.Label(root, text="y2:").place(x=500, y=50)
    y2_entry = tk.Entry(root, width=5)
    y2_entry.place(x=530, y=50)

    # Botón aplicar recorte
    btn_aplicar = tk.Button(root, text="Aplicar recorte",
                            command=lambda: aplicar_recorte(x1_entry, y1_entry, x2_entry, y2_entry))
    btn_aplicar.place(x=420, y=80)

    # Guardar widgets para luego borrarlos
    widgets_dinamicos = [x1_entry, y1_entry, x2_entry, y2_entry, btn_aplicar]


def aplicar_recorte(x1_entry, y1_entry, x2_entry, y2_entry):
    """Realiza el recorte según los valores ingresados."""
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    try:
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Introduce valores numéricos válidos.")
        return

    img_np = np.array(img_original)
    resultado = ip.recortar_imagen(img_np, x1, y1, x2, y2)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada)

    limpiar_widgets()  # limpia las cajas después del recorte

def modo_zoom():
    """Activa el modo de zoom con entradas de coordenadas y factor."""
    limpiar_widgets()
    global widgets_dinamicos

    # Etiquetas y entradas de coordenadas
    tk.Label(root, text="x1:").place(x=420, y=20)
    x1_entry = tk.Entry(root, width=5)
    x1_entry.place(x=450, y=20)

    tk.Label(root, text="y1:").place(x=500, y=20)
    y1_entry = tk.Entry(root, width=5)
    y1_entry.place(x=530, y=20)

    tk.Label(root, text="x2:").place(x=420, y=50)
    x2_entry = tk.Entry(root, width=5)
    x2_entry.place(x=450, y=50)

    tk.Label(root, text="y2:").place(x=500, y=50)
    y2_entry = tk.Entry(root, width=5)
    y2_entry.place(x=530, y=50)

    # Entrada para el factor de zoom
    tk.Label(root, text="Escala:").place(x=420, y=80)
    escala_entry = tk.Entry(root, width=5)
    escala_entry.insert(0, "2")  # valor por defecto
    escala_entry.place(x=480, y=80)

    # Botón para aplicar zoom
    btn_aplicar_zoom = tk.Button(root, text="Aplicar Zoom",
                                 command=lambda: aplicar_zoom(
                                     x1_entry, y1_entry, x2_entry, y2_entry, escala_entry))
    btn_aplicar_zoom.place(x=420, y=110)

    widgets_dinamicos = [x1_entry, y1_entry, x2_entry, y2_entry, escala_entry, btn_aplicar_zoom]


def aplicar_zoom(x1_entry, y1_entry, x2_entry, y2_entry, escala_entry):
    """Aplica el zoom al área seleccionada."""
    global img_original, img_procesada
    if img_original is None:
        messagebox.showwarning("Atención", "Primero abre una imagen.")
        return

    try:
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        escala = float(escala_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Introduce valores numéricos válidos.")
        return

    img_np = np.array(img_original)
    resultado = ip.zoom_area(img_np, x1, y1, x2, y2, escala)
    img_procesada = Image.fromarray(resultado)
    mostrar_imagen(img_procesada)

    limpiar_widgets()  # limpia los widgets después del zoom

def interfaz_rotar():
    limpiar_widgets()
    
    lbl_angulo = tk.Label(root, text="Ángulo de rotación (°):")
    lbl_angulo.place(x=650, y=80)
    entry_angulo = tk.Entry(root, width=10)
    entry_angulo.place(x=800, y=80)

    def aplicar_rotacion():
        global img_original
        try:
            angulo = float(entry_angulo.get())
        except ValueError:
            return
        if img_original is None:
            return
        img_np = np.array(img_original)
        rotada = ip.rotar_imagen(img_np, angulo)
        img_procesada = Image.fromarray(rotada)
        mostrar_imagen(img_procesada)

    btn_aplicar = tk.Button(root, text="Aplicar rotación", command=aplicar_rotacion)
    btn_aplicar.place(x=740, y=120)

    widgets_dinamicos.extend([lbl_angulo, entry_angulo, btn_aplicar])
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

#brillo
slider_brillo = tk.Scale(root, from_=-1, to= 1, resolution= 0.01, orient= tk.HORIZONTAL, length= 220, command= aplicar_brillo_btn)

slider_brillo.set(0.0)
slider_brillo.place(x = 420, y = 5)

#contraste log
boton_contraste_log = tk.Button(root, text= "Aplicar contraste logaritmico",command=aplicar_log)
boton_contraste_log.place(x=500,y=200)

#contraste exponencial
boton_contraste_exp = tk.Button(root, text= "Aplicar contraste exponencial",command=aplicar_exp)
boton_contraste_exp.place(x=500,y=250)

#boton recorte
btn_recorte = tk.Button(root, text="Recortar imagen", command=modo_recorte)
btn_recorte.place(x=240, y=20)

#boton zoom
btn_zoom = tk.Button(root, text="zoom a la imagen", command=modo_zoom)
btn_zoom.place(x=240, y=500)

#boton rotar imagen
btn_rotar = tk.Button(root, text="Rotar imagen", command=interfaz_rotar)
btn_rotar.place(x=240, y=300)



root.mainloop()
