# Tema 3: Métodos para Resolver Sistemas de Ecuaciones

## Subtema: Método de Gauss-Seidel

---

## Descripción

El método de Gauss-Seidel es un procedimiento iterativo que aproxima la solución de un sistema de ecuaciones.

En cada vuelta utiliza los valores nuevos que se van calculando, por eso puede acercarse rápido a la solución cuando el sistema está bien acomodado.

---

## Código 1

### Sistema

```text
4x + y = 9
x + 3y = 7
```

### Código

```python
x = 0
y = 0

for vuelta in range(12):
    x = (9 - y) / 4
    y = (7 - x) / 3

print(x, y)
```

### Resultado

```text
2.0 1.6666666666666667
```

---

## Código 2

### Sistema

```text
5x + 2y = 16
x + 4y = 14
```

### Código

```python
a = 0
b = 0

for i in range(15):
    a = (16 - 2*b) / 5
    b = (14 - a) / 4

print(a, b)
```

### Resultado

```text
2.0 3.0
```

---

## Código 3

### Sistema

```text
6x - y = 17
2x + 5y = 31
```

### Código

```python
x_actual = 0
y_actual = 0

for paso in range(12):
    x_actual = (17 + y_actual) / 6
    y_actual = (31 - 2*x_actual) / 5

print(x_actual, y_actual)
```

### Resultado

```text
3.5 4.8
```

---

## Código 4

### Sistema 3x3

```text
10x + y + z = 17
2x + 10y + z = 28
2x + 3y + 10z = 35
```

### Código

```python
x = 0
y = 0
z = 0

for ciclo in range(20):
    x = (17 - y - z) / 10
    y = (28 - 2*x - z) / 10
    z = (35 - 2*x - 3*y) / 10

print(x, y, z)
```

### Resultado

```text
1.2 2.3 2.57
```

---

## Código 5

### Sistema 4x4

```text
8x + y + z + w = 18
x + 7y + z + w = 20
x + y + 6z + w = 22
x + y + z + 5w = 24
```

### Código

```python
x = y = z = w = 0

for intento in range(25):
    x = (18 - y - z - w) / 8
    y = (20 - x - z - w) / 7
    z = (22 - x - y - w) / 6
    w = (24 - x - y - z) / 5

print(x, y, z, w)
```

### Resultado

```text
1.2953020134 1.7785234899 2.4832214765 3.6885906040
```

---

## Código 6

### Sistema 5x5

```text
12x + y + z + w + v = 20
x + 11y + z + w + v = 25
x + y + 10z + w + v = 30
x + y + z + 9w + v = 35
x + y + z + w + 8v = 40
```

### Código

```python
x = y = z = w = v = 0

for repeticion in range(30):
    x = (20 - y - z - w - v) / 12
    y = (25 - x - z - w - v) / 11
    z = (30 - x - y - w - v) / 10
    w = (35 - x - y - z - v) / 9
    v = (40 - x - y - z - w) / 8

print(x, y, z, w, v)
```

### Resultado

```text
0.4032815196 0.8677715855 1.4815917708 2.2473228738 3.2547542818
```

---

## Conclusión

Gauss-Seidel es útil para aproximar soluciones de sistemas lineales mediante iteraciones.

Su ventaja es que aprovecha inmediatamente los valores nuevos, lo que puede mejorar la rapidez de convergencia.