# Tema 5: Interpolación y Ajuste de Funciones

## Subtema: Interpolación Cuadrática

---

## Descripción

La interpolación cuadrática permite estimar valores intermedios utilizando tres puntos conocidos.

A diferencia de la interpolación lineal, este método genera una parábola que pasa por los tres puntos de referencia, obteniendo generalmente una mejor aproximación.

---

## Código 1

### Datos

```text
(0,1)
(2,5)
(4,17)

x = 3
```

### Código

```python
def interpolar(valor):

    a = 0
    b = 1

    c = 2
    d = 5

    e = 4
    f = 17

    termino1 = b * ((valor - c)*(valor - e)) / ((a - c)*(a - e))
    termino2 = d * ((valor - a)*(valor - e)) / ((c - a)*(c - e))
    termino3 = f * ((valor - a)*(valor - c)) / ((e - a)*(e - c))

    return termino1 + termino2 + termino3

print(interpolar(3))
```

### Resultado

```text
10.0
```

### Explicación

Se construye una parábola utilizando tres puntos conocidos y después se evalúa en el valor deseado.

---

## Código 2

### Datos

```text
(1,3)
(2,8)
(4,24)

x = 3
```

### Código

```python
def calcular(x):

    x1 = 1
    y1 = 3

    x2 = 2
    y2 = 8

    x3 = 4
    y3 = 24

    p1 = y1 * ((x - x2)*(x - x3)) / ((x1 - x2)*(x1 - x3))
    p2 = y2 * ((x - x1)*(x - x3)) / ((x2 - x1)*(x2 - x3))
    p3 = y3 * ((x - x1)*(x - x2)) / ((x3 - x1)*(x3 - x2))

    return p1 + p2 + p3

print(calcular(3))
```

### Resultado

```text
15.0
```

### Explicación

La interpolación cuadrática aprovecha la información de tres puntos para representar mejor la tendencia de los datos.

---

## Código 3

### Datos

```text
(1,2)
(3,6)
(5,18)

x = 4
```

### Código

```python
def funcion(valor):

    punto1 = 1
    dato1 = 2

    punto2 = 3
    dato2 = 6

    punto3 = 5
    dato3 = 18

    r1 = dato1 * ((valor - punto2)*(valor - punto3)) / ((punto1 - punto2)*(punto1 - punto3))
    r2 = dato2 * ((valor - punto1)*(valor - punto3)) / ((punto2 - punto1)*(punto2 - punto3))
    r3 = dato3 * ((valor - punto1)*(valor - punto2)) / ((punto3 - punto1)*(punto3 - punto2))

    return r1 + r2 + r3

print(funcion(4))
```

### Resultado

```text
11.0
```

### Explicación

La parábola generada pasa exactamente por los tres puntos proporcionados.

---

## Código 4

### Datos

```text
(2,4)
(4,12)
(6,28)

x = 5
```

### Código

```python
def aproximar(x):

    xa = 2
    ya = 4

    xb = 4
    yb = 12

    xc = 6
    yc = 28

    t1 = ya * ((x - xb)*(x - xc)) / ((xa - xb)*(xa - xc))
    t2 = yb * ((x - xa)*(x - xc)) / ((xb - xa)*(xb - xc))
    t3 = yc * ((x - xa)*(x - xb)) / ((xc - xa)*(xc - xb))

    return t1 + t2 + t3

print(aproximar(5))
```

### Resultado

```text
19.0
```

### Explicación

La interpolación cuadrática puede adaptarse mejor a datos curvos que la interpolación lineal.

---

## Código 5

### Datos

```text
(0,0)
(2,4)
(4,16)

x = 3
```

### Código

```python
def evaluar(x):

    x0 = 0
    y0 = 0

    x1 = 2
    y1 = 4

    x2 = 4
    y2 = 16

    a = y0 * ((x - x1)*(x - x2)) / ((x0 - x1)*(x0 - x2))
    b = y1 * ((x - x0)*(x - x2)) / ((x1 - x0)*(x1 - x2))
    c = y2 * ((x - x0)*(x - x1)) / ((x2 - x0)*(x2 - x1))

    return a + b + c

print(evaluar(3))
```

### Resultado

```text
9.0
```

### Explicación

Este método es especialmente útil cuando los datos presentan una tendencia parabólica.

---

## Conclusión

La interpolación cuadrática utiliza tres puntos para construir una parábola que permite estimar valores intermedios con mayor precisión que la interpolación lineal.

Es una herramienta muy utilizada en análisis numérico cuando la relación entre los datos no sigue una línea recta.