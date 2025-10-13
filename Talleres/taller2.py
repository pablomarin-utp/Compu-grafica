import numpy as np

"""
Ejercicio 1: Creación de arrays
Crea un array 1D con los valores [12, 45, 78, 34, 56] y:
1. Muestra el array.
2. Muestra su tipo de datos (dtype).
3. Muestra el número de dimensiones (ndim) y su forma (shape).

"""

arr = np.array([12, 45, 78, 34, 56])
print("Array:", arr)
print("Tipo de datos (dtype):", arr.dtype)
print("Número de dimensiones (ndim):", arr.ndim)
print("Forma (shape):", arr.shape)

"""
Ejercicio 2: Arrays 2D y propiedades
Crea un array 2D con la siguiente lista de listas:
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]
Luego:
1. Muestra el número de elementos (size).
2. Cambia el tipo de datos a float32.
3. Muestra el nuevo array.
"""

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],  
                   [7, 8, 9]])

print("\nArray 2D:\n", arr_2d)
print("Número de elementos (size):", arr_2d.size)
arr_2d = arr_2d.astype(np.float32)
print("Nuevo array con tipo de datos float32:\n", arr_2d)

"""
Ejercicio 3: Arrays especiales
Usa funciones de NumPy para:
1. Crear un array de ceros de tamaño (2, 4).
2. Crear un array de unos de tamaño (3, 3).
3. Crear un array con valores del 10 al 50, con paso de 5.
4. Crear un array con 8 valores equidistantes entre 0 y 1.
"""

arr_zeros = np.zeros((2, 4))
arr_ones = np.ones((3, 3))
arr_range = np.arange(10, 55, 5)
arr_linspace = np.linspace(0, 1, 8)

"""
Ejercicio 4: Operaciones matemáticas
Crea dos arrays 1D:
- a con valores [2, 4, 6, 8, 10]
- b con valores [1, 3, 5, 7, 9]
Realiza y muestra:
1. Suma
2. Resta
3. Multiplicación elemento a elemento
4. División elemento a element
"""

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 3, 5, 7, 9])

print("\nSuma:", a + b)
print("Resta:", a - b)
print("Multiplicación elemento a elemento:", a * b)
print("División elemento a elemento:", a / b)


"""
Ejercicio 5: Funciones de agregación
Crea un array con valores enteros del 1 al 20 y calcula:
1. La suma total.
2. El valor máximo y mínimo.
3. El promedio.
4. La desviación estándar (np.std()).
"""

arr_agg = np.arange(1, 21)

print("Suma total:", np.sum(arr_agg))
print("Valor máximo:", np.max(arr_agg))
print("Valor mínimo:", np.min(arr_agg))
print("Promedio:", np.mean(arr_agg))
print("Desviación estándar:", np.std(arr_agg))

"""
Ejercicio 6: Indexación y slicing
Dado el array:
[[5, 10, 15],
[20, 25, 30],
[35, 40, 45],
[50, 55, 60]]
Realiza:
1. Extrae la primera columna.
2. Extrae la tercera fila.
3. Obtén una submatriz de las últimas dos filas y las últimas dos columnas.
"""

arr_index = np.array([[5, 10, 15],
                      [20, 25, 30], 
                      [35, 40, 45], 
                      [50, 55, 60]])

print("\nPrimera columna:", arr_index[:, 0])
print("Tercera fila:", arr_index[2, :])
print("Submatriz de las últimas dos filas y últimas dos columnas:\n", arr_index[-2:, -2:])

"""
Ejercicio 7: Números aleatorios
Usa np.random para:
1. Generar 10 números aleatorios entre 0 y 1.
2. Generar una matriz 4x4 con enteros aleatorios entre 50 y 100.
3. Generar 1000 valores con distribución normal y mostrar su promedio y desviación
estándar.
"""

random_floats = np.random.rand(10)
random_ints = np.random.randint(50, 100, (4, 4))
normal_dist = np.random.randn(1000)

print("\nPromedio de distribución normal:", np.mean(normal_dist))
print("Desviación estándar de distribución normal:", np.std(normal_dist))
