# Tema 3: Métodos para Resolver Sistemas de Ecuaciones

## Subtema: Método de Gauss-Jordan

---

## Descripción

El método de Gauss-Jordan permite resolver sistemas lineales transformando la matriz aumentada hasta convertir la parte de coeficientes en una matriz identidad.

Cuando termina el proceso, los valores de las incógnitas aparecen directamente en la última columna.

---

## Código 1

### Sistema

```text
3x + y = 11
x - y = 1
```

### Código

```python
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
```

### Resultado

```text
[[1. 0. 3.]
 [0. 1. 2.]]
```

---

## Código 2

### Sistema

```text
4x + 2y = 22
x - y = 2
```

### Código

```python
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
```

### Resultado

```text
[[1. 0. 4.33333333]
 [0. 1. 2.33333333]]
```

---

## Código 3

### Sistema

```text
5x - y = 13
2x + y = 8
```

### Código

```python
import numpy as np

datos = np.array([
    [5, -1, 13],
    [2, 1, 8]
], dtype=float)

n = len(datos)

for fila in range(n):
    datos[fila] = datos[fila] / datos[fila][fila]

    for columna in range(n):
        if fila != columna:
            factor = datos[columna][fila]
            datos[columna] = datos[columna] - factor * datos[fila]

print(datos)
```

### Resultado

```text
[[1. 0. 3.]
 [0. 1. 2.]]
```

---

## Código 4

### Sistema 5x5

```text
x + y + z + w + v = 20
2x + y - z + w + v = 18
x - y + 2z + w - v = 10
3x + y + z - w + 2v = 25
x + 2y + z + 3w + v = 30
```

### Código

```python
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
```

### Resultado

```text
[[1.         0.         0.         0.         0.         4.92307692]
 [0.         1.         0.         0.         0.         5.23076923]
 [0.         0.         1.         0.         0.         4.15384615]
 [0.         0.         0.         1.         0.         4.38461538]
 [0.         0.         0.         0.         1.         1.30769231]]
```

---

## Código 5

### Sistema 5x5

```text
2x + y + z - w + v = 12
x + 4y - z + w + 2v = 20
3x - y + 2z + w - v = 15
x + y + 3z + 2w + v = 25
2x - 2y + z + 3w + v = 18
```

### Código

```python
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
```

### Resultado

```text
[[1.         0.         0.         0.         0.         3.27433628]
 [0.         1.         0.         0.         0.         3.17699115]
 [0.         0.         1.         0.         0.         4.13274336]
 [0.         0.         0.         1.         0.         2.63716814]
 [0.         0.         0.         0.         1.         1.87610619]]
```

---

## Código 6

### Sistema 5x5

```text
x + 3y + z - w + v = 14
2x - y + 2z + w + v = 16
3x + y - z + 2w - v = 11
x - 2y + 3z + w + 2v = 19
2x + y + w + 3v = 21
```

### Código

```python
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
```

### Resultado

```text
[[1.         0.         0.         0.         0.         3.61428571]
 [0.         1.         0.         0.         0.         2.21428571]
 [0.         0.         1.         0.         0.         3.3       ]
 [0.         0.         0.         1.         0.         0.04285714]
 [0.         0.         0.         0.         1.         3.87142857]]
```

---

## Conclusión

Gauss-Jordan es útil porque reduce la matriz aumentada hasta una forma donde la solución se puede leer directamente.

A diferencia de la eliminación gaussiana, este método no necesita sustitución hacia atrás.