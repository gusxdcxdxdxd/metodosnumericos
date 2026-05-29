import numpy as np

matriz = np.array([
    [3, 1, 11],
    [1, -1, 1]
], dtype=float)

n = len(matriz)

for i in range(n):
    matriz[i] = matriz[i] / matriz[i][i]

    for j in range(n):
        if i != j:
            factor = matriz[j][i]
            matriz[j] = matriz[j] - factor * matriz[i]

print(matriz)