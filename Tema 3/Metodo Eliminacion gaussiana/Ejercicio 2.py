import numpy as np

coeficientes = np.array([
    [4, 2],
    [1, -1]
], dtype=float)

terminos = np.array([18, 1], dtype=float)

respuesta = np.linalg.solve(coeficientes, terminos)

print(respuesta)