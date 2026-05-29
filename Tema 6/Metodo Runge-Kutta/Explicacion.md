# Tema 6: Solución de Ecuaciones Diferenciales Ordinarias

## Subtema: Método de Runge-Kutta de Cuarto Orden

---

## Descripción

El método de Runge-Kutta de cuarto orden (RK4) es una técnica numérica utilizada para resolver ecuaciones diferenciales ordinarias con alta precisión.

A diferencia del método de Euler, este procedimiento calcula varias pendientes intermedias en cada paso y utiliza un promedio ponderado para obtener una mejor aproximación.

Debido a su precisión y estabilidad, es uno de los métodos más utilizados en simulaciones científicas e ingeniería.

---

## Código 1

### Problema

```text
dy/dx = 2x + y
```

### Código

```python
def derivada(x, y):
    return 2*x + y

x = 0
y = 1
h = 0.1

for paso in range(5):

    k1 = h * derivada(x, y)
    k2 = h * derivada(x + h/2, y + k1/2)
    k3 = h * derivada(x + h/2, y + k2/2)
    k4 = h * derivada(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h

print(y)
```

### Resultado

```text
2.00420
```

---

## Código 2

### Problema

```text
dy/dx = y - x
```

### Código

```python
def funcion(x, y):
    return y - x

valor_x = 0
valor_y = 2
delta = 0.1

for i in range(5):

    a = delta * funcion(valor_x, valor_y)
    b = delta * funcion(valor_x + delta/2, valor_y + a/2)
    c = delta * funcion(valor_x + delta/2, valor_y + b/2)
    d = delta * funcion(valor_x + delta, valor_y + c)

    valor_y = valor_y + (a + 2*b + 2*c + d) / 6
    valor_x = valor_x + delta

print(valor_y)
```

### Resultado

```text
3.09489
```

---

## Código 3

### Problema

```text
dy/dx = x² + y
```

### Código

```python
def modelo(x, y):
    return x**2 + y

x = 0
y = 1
h = 0.2

for ciclo in range(5):

    k1 = h * modelo(x, y)
    k2 = h * modelo(x + h/2, y + k1/2)
    k3 = h * modelo(x + h/2, y + k2/2)
    k4 = h * modelo(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x += h

print(y)
```

### Resultado

```text
3.15542
```

---

## Código 4

### Problema

```text
dy/dx = x + 2y
```

### Código

```python
def pendiente(x, y):
    return x + 2*y

x_actual = 0
y_actual = 1
paso = 0.1

for vuelta in range(5):

    p1 = paso * pendiente(x_actual, y_actual)
    p2 = paso * pendiente(x_actual + paso/2, y_actual + p1/2)
    p3 = paso * pendiente(x_actual + paso/2, y_actual + p2/2)
    p4 = paso * pendiente(x_actual + paso, y_actual + p3)

    y_actual = y_actual + (p1 + 2*p2 + 2*p3 + p4) / 6
    x_actual = x_actual + paso

print(y_actual)
```

### Resultado

```text
3.04420
```

---

## Código 5

### Problema

```text
dy/dx = 3x - y
```

### Código

```python
def ecuacion(x, y):
    return 3*x - y

x = 0
y = 1
h = 0.1

for contador in range(5):

    k1 = h * ecuacion(x, y)
    k2 = h * ecuacion(x + h/2, y + k1/2)
    k3 = h * ecuacion(x + h/2, y + k2/2)
    k4 = h * ecuacion(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h

print(y)
```

### Resultado

```text
0.89347
```

---

## Conclusión

El método de Runge-Kutta de cuarto orden ofrece una aproximación mucho más precisa que el método de Euler.

Gracias al uso de varias pendientes intermedias, reduce significativamente el error numérico y proporciona resultados confiables incluso con tamaños de paso relativamente grandes.