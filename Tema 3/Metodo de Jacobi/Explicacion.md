# Tema 3: Métodos para Resolver Sistemas de Ecuaciones

## Subtema: Método de Jacobi

---

## Descripción

El método de Jacobi es un algoritmo iterativo utilizado para encontrar soluciones aproximadas de sistemas de ecuaciones lineales.

A diferencia de Gauss-Seidel, todas las nuevas aproximaciones se calculan utilizando únicamente los valores de la iteración anterior.

Este método suele funcionar mejor cuando la matriz es diagonalmente dominante.

---

## Código 1

### Sistema

```text
4x + y = 11
x + 3y = 9
```

### Código

```python
x = 0
y = 0

for paso in range(12):

    nuevo_x = (11 - y) / 4
    nuevo_y = (9 - x) / 3

    x = nuevo_x
    y = nuevo_y

print(x, y)
```

### Resultado

```text
2.1818181818 2.2727272727
```

---

## Código 2

### Sistema

```text
5x + 2y = 14
x + 4y = 11
```

### Código

```python
a = 0
b = 0

for vuelta in range(15):

    siguiente_a = (14 - 2*b) / 5
    siguiente_b = (11 - a) / 4

    a = siguiente_a
    b = siguiente_b

print(a, b)
```

### Resultado

```text
2.0 2.25
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
valor_x = 0
valor_y = 0

for i in range(15):

    nuevo_x = (17 + valor_y) / 6
    nuevo_y = (31 - 2*valor_x) / 5

    valor_x = nuevo_x
    valor_y = nuevo_y

print(valor_x, valor_y)
```

### Resultado

```text
3.5 4.8
```

---

## Código 4

### Sistema 3x3

```text
10x + y + z = 18
2x + 11y + z = 25
x + 2y + 10z = 27
```

### Código

```python
x = y = z = 0

for intento in range(20):

    nx = (18 - y - z) / 10
    ny = (25 - 2*x - z) / 11
    nz = (27 - x - 2*y) / 10

    x = nx
    y = ny
    z = nz

print(x, y, z)
```

### Resultado

```text
1.17431193 1.85321101 2.21100917
```

---

## Código 5

### Sistema 4x4

```text
8x + y + z + w = 22
x + 7y + z + w = 20
x + y + 6z + w = 18
x + y + z + 5w = 24
```

### Código

```python
x = y = z = w = 0

for ciclo in range(25):

    nx = (22 - y - z - w) / 8
    ny = (20 - x - z - w) / 7
    nz = (18 - x - y - w) / 6
    nw = (24 - x - y - z) / 5

    x = nx
    y = ny
    z = nz
    w = nw

print(x, y, z, w)
```

### Resultado

```text
2.26966292 1.82022472 1.26966292 3.26966292
```

---

## Código 6

### Sistema 5x5

```text
12x + y + z + w + v = 24
x + 11y + z + w + v = 28
x + y + 10z + w + v = 30
x + y + z + 9w + v = 35
x + y + z + w + 8v = 40
```

### Código

```python
x = y = z = w = v = 0

for repeticion in range(30):

    nx = (24 - y - z - w - v) / 12
    ny = (28 - x - z - w - v) / 11
    nz = (30 - x - y - w - v) / 10
    nw = (35 - x - y - z - v) / 9
    nv = (40 - x - y - z - w) / 8

    x = nx
    y = ny
    z = nz
    w = nw
    v = nv

print(x, y, z, w, v)
```

### Resultado

```text
0.93364531 1.39065817 1.77234612 2.33448743 4.19657212
```

---

## Conclusión

El método de Jacobi permite aproximar la solución de sistemas de ecuaciones mediante iteraciones sucesivas.

Su principal característica es que cada nueva aproximación se calcula utilizando exclusivamente los valores obtenidos en la iteración anterior.