# Editor de Imágenes - Compu-grafica

Este proyecto es una aplicación de escritorio en Python para la edición básica de imágenes, desarrollada con Tkinter y NumPy. Permite aplicar transformaciones y efectos sobre imágenes de forma visual e interactiva.

## Características principales
- Ajuste de brillo global y por canal (R, G, B)
- Contraste logarítmico y exponencial
- Negativo, escala de grises y binarización
- Visualización de histograma RGB
- Recorte y zoom de área
- Extracción de capas RGB y CMYK (coloreadas)
- Rotación en múltiplos de 90°
- Fusión de imágenes (simple y ecualizada)
- Guardado del resultado
- Panel de controles con scrollbar para fácil navegación

## Requisitos
- Python 3.8+
- Paquetes: numpy, pillow, matplotlib

Puedes instalar los requisitos con:
```bash
pip install numpy pillow matplotlib
```

## Uso
1. Ejecuta la aplicación principal:
   ```bash
   python libreria/proyecto_tkinter.py
   ```
2. Abre una imagen desde el menú "Archivo".
3. Usa los controles del panel izquierdo para aplicar transformaciones.
4. Visualiza el resultado en el área derecha.
5. Guarda el resultado desde el menú "Archivo".

## Estructura del proyecto
```
Compu-grafica/
├── main.py                # Script principal (no GUI)
├── libreria/
│   ├── main.py            # Funciones de procesamiento de imagen
│   ├── proyecto_tkinter.py# Interfaz gráfica principal
│   └── ...                # Otros módulos
└── Talleres/              # Ejercicios y talleres
```

## Autor
Pablo Marín

## Licencia
Uso educativo.
