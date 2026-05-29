import numpy as np

tabla = np.array([
    [1, 3, 1, -1, 1, 14],
    [2, -1, 2, 1, 1, 16],
    [3, 1, -1, 2, -1, 11],
    [1, -2, 3, 1, 2, 19],
    [2, 1, 0, 1, 3, 21]
], dtype=float)

n = len(tabla)

for i in range(n):
    tabla[i] = tabla[i] / tabla[i][i]

    for j in range(n):
        if i != j:
            factor = tabla[j][i]
            tabla[j] = tabla[j] - factor * tabla[i]

print(tabla)