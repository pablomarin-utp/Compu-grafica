import plot_utils
import rgb_manip

gato = plot_utils.image_from_path("gaot.png")
plot_utils.show_image(gato, "Gato png")


moño = plot_utils.image_from_path("moño.jpg")
gatito = plot_utils.image_from_path("gatito.jpg")

combined = rgb_manip.combine_norezise(moño, gatito, (100,90), 0.5)  
plot_utils.show_image(combined, "Combinada")

inverted = rgb_manip.invert(gatito)
plot_utils.show_image(inverted, "Invertida")        

gray = rgb_manip.gray_scale(gatito)
plot_utils.show_image(gray, "Escala de grises", cmap="gray")