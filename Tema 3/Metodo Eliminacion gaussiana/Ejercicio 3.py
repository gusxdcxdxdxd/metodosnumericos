import numpy as np

A = np.array([
    [5, -2],
    [1, 1]
], dtype=float)

B = np.array([16, 5], dtype=float)

valores = np.linalg.solve(A, B)

print(valores)