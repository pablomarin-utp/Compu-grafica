import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    
    route = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*")])
    
    if not route:
        return
    
    img = Image.open(route)
    img_resized = img.resize((300, 300))

    img = ImageTk.PhotoImage(img_resized)

    lbl.config(image=img)
    lbl.image = img

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x600")

btn = tk.Button(root, text="Open Image", command=open_image)
btn.place(x=0, y=0)

lbl = tk.Label(root)
lbl.place(x=150, y=50)

root.mainloop()