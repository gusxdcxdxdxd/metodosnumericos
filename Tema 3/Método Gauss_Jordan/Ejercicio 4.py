import numpy as np

sistema = np.array([
    [1, 1, 1, 1, 1, 20],
    [2, 1, -1, 1, 1, 18],
    [1, -1, 2, 1, -1, 10],
    [3, 1, 1, -1, 2, 25],
    [1, 2, 1, 3, 1, 30]
], dtype=float)

n = len(sistema)

for i in range(n):
    sistema[i] = sistema[i] / sistema[i][i]

    for j in range(n):
        if i != j:
            factor = sistema[j][i]
            sistema[j] = sistema[j] - factor * sistema[i]

print(sistema)