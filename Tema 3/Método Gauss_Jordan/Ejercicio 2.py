import numpy as np

tabla = np.array([
    [4, 2, 22],
    [1, -1, 2]
], dtype=float)

n = len(tabla)

for i in range(n):
    tabla[i] = tabla[i] / tabla[i][i]

    for j in range(n):
        if i != j:
            valor = tabla[j][i]
            tabla[j] = tabla[j] - valor * tabla[i]

print(tabla)