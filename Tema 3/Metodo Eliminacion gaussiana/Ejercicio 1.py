import numpy as np

matriz = np.array([
    [3, 1],
    [2, -1]
], dtype=float)

resultado = np.array([10, 5], dtype=float)

solucion = np.linalg.solve(matriz, resultado)

print(solucion)