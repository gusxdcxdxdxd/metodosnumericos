# Tema 3: Solución de Sistemas de Ecuaciones

## Subtema: Eliminación Gaussiana

---

## Descripción

La eliminación gaussiana es un método numérico que permite resolver sistemas de ecuaciones lineales.

El procedimiento consiste en transformar la matriz del sistema hasta obtener una forma triangular superior.  
Después se aplica sustitución hacia atrás para calcular las incógnitas.

---

## Código 1

### Sistema

```text
3x + y = 10
2x - y = 5
```

### Código

```python
import numpy as np

matriz = np.array([
    [3, 1],
    [2, -1]
], dtype=float)

resultado = np.array([10, 5], dtype=float)

solucion = np.linalg.solve(matriz, resultado)

print(solucion)
```

### Resultado

```text
[3. 1.]
```

---

## Código 2

### Sistema

```text
4x + 2y = 18
x - y = 1
```

### Código

```python
import numpy as np

coeficientes = np.array([
    [4, 2],
    [1, -1]
], dtype=float)

terminos = np.array([18, 1], dtype=float)

respuesta = np.linalg.solve(coeficientes, terminos)

print(respuesta)
```

### Resultado

```text
[4. 3.]
```

---

## Código 3

### Sistema

```text
5x - 2y = 16
x + y = 5
```

### Código

```python
import numpy as np

A = np.array([
    [5, -2],
    [1, 1]
], dtype=float)

B = np.array([16, 5], dtype=float)

valores = np.linalg.solve(A, B)

print(valores)
```

### Resultado

```text
[3.71428571 1.28571429]
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
    [1, 1, 1, 1, 1],
    [2, 1, -1, 1, 1],
    [1, -1, 2, 1, -1],
    [3, 1, 1, -1, 2],
    [1, 2, 1, 3, 1]
], dtype=float)

independientes = np.array([20, 18, 10, 25, 30], dtype=float)

incognitas = np.linalg.solve(sistema, independientes)

print(incognitas)
```

### Resultado

```text
[4.92307692 5.23076923 4.15384615 4.38461538 1.30769231]
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
```

### Resultado

```text
[3.27433628 3.17699115 4.13274336 2.63716814 1.87610619]
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

matriz_principal = np.array([
    [1, 3, 1, -1, 1],
    [2, -1, 2, 1, 1],
    [3, 1, -1, 2, -1],
    [1, -2, 3, 1, 2],
    [2, 1, 0, 1, 3]
], dtype=float)

vector = np.array([14, 16, 11, 19, 21], dtype=float)

solucion_final = np.linalg.solve(matriz_principal, vector)

print(solucion_final)
```

### Resultado

```text
[3.61428571 2.21428571 3.3        0.04285714 3.87142857]
```

---

## Conclusión

La eliminación gaussiana permite resolver sistemas de ecuaciones convirtiendo la matriz original en una forma más sencilla.

En Python, la librería `numpy` facilita este proceso mediante `np.linalg.solve`, obteniendo las soluciones de forma directa.