import numpy as np

sistema = np.array([
    [1, 1, 1, 1, 1],
    [2, 1, -1, 1, 1],
    [1, -1, 2, 1, -1],
    [3, 1, 1, -1, 2],
    [1, 2, 1, 3, 1]
], dtype=float)

independientes = np.array([20, 18, 10, 25, 30], dtype=float)

incognitas = np.linalg.solve(sistema, independientes)

print(incognitas)