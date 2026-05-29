import numpy as np

datos = np.array([
    [2, 1, 1, -1, 1],
    [1, 4, -1, 1, 2],
    [3, -1, 2, 1, -1],
    [1, 1, 3, 2, 1],
    [2, -2, 1, 3, 1]
], dtype=float)

res = np.array([12, 20, 15, 25, 18], dtype=float)

x = np.linalg.solve(datos, res)

print(x)