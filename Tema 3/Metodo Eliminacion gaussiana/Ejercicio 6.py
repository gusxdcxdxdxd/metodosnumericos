import numpy as np

matriz_principal = np.array([
    [1, 3, 1, -1, 1],
    [2, -1, 2, 1, 1],
    [3, 1, -1, 2, -1],
    [1, -2, 3, 1, 2],
    [2, 1, 0, 1, 3]
], dtype=float)

vector = np.array([14, 16, 11, 19, 21], dtype=float)

solucion_final = np.linalg.solve(matriz_principal, vector)

print(solucion_final)