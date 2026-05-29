import numpy as np

matriz_aumentada = np.array([
    [2, 1, 1, -1, 1, 12],
    [1, 4, -1, 1, 2, 20],
    [3, -1, 2, 1, -1, 15],
    [1, 1, 3, 2, 1, 25],
    [2, -2, 1, 3, 1, 18]
], dtype=float)

n = len(matriz_aumentada)

for i in range(n):
    matriz_aumentada[i] = matriz_aumentada[i] / matriz_aumentada[i][i]

    for j in range(n):
        if i != j:
            factor = matriz_aumentada[j][i]
            matriz_aumentada[j] = matriz_aumentada[j] - factor * matriz_aumentada[i]

print(matriz_aumentada)