import numpy as np

datos = np.array([
    [5, -1, 13],
    [2, 1, 8]
], dtype=float)

n = len(datos)

for fila in range(n):
    datos[fila] = datos[fila] / datos[fila][fila]

    for columna in range(n):
        if fila != columna:
            factor = datos[columna][fila]
            datos[columna] = datos[columna] - factor * datos[fila]

print(datos)