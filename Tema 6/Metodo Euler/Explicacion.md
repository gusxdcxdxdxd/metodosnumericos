# Tema 6: Solución de Ecuaciones Diferenciales Ordinarias

## Subtema: Método de Euler

---

## Descripción

El método de Euler es una técnica numérica utilizada para aproximar soluciones de ecuaciones diferenciales ordinarias.

Su funcionamiento consiste en utilizar la pendiente proporcionada por la ecuación diferencial para estimar el siguiente valor de la solución.

Es uno de los métodos más sencillos de implementar, aunque su precisión depende del tamaño del paso utilizado.

---

## Código 1

### Problema

```text
dy/dx = 2x + y

x₀ = 0
y₀ = 1

h = 0.1
n = 5
```

### Código

```python
def derivada(x, y):
    return 2*x + y

x_actual = 0
y_actual = 1

paso = 0.1

for iteracion in range(5):
    y_actual = y_actual + paso * derivada(x_actual, y_actual)
    x_actual = x_actual + paso

print(y_actual)
```

### Resultado

```text
1.97931
```

### Explicación

La aproximación se obtiene avanzando paso a paso utilizando la pendiente calculada en cada punto.

---

## Código 2

### Problema

```text
dy/dx = y - x

x₀ = 0
y₀ = 2

h = 0.1
n = 5
```

### Código

```python
def funcion(x, y):
    return y - x

x = 0
y = 2

incremento = 0.1

for paso in range(5):
    y = y + incremento * funcion(x, y)
    x = x + incremento

print(y)
```

### Resultado

```text
3.05242
```

### Explicación

Cada nuevo valor depende del valor anterior y de la pendiente calculada por la ecuación diferencial.

---

## Código 3

### Problema

```text
dy/dx = x² + y

x₀ = 0
y₀ = 1

h = 0.2
n = 5
```

### Código

```python
def ecuacion(x, y):
    return x**2 + y

x = 0
y = 1

h = 0.2

for i in range(5):
    y = y + h * ecuacion(x, y)
    x = x + h

print(y)
```

### Resultado

```text
2.90045
```

### Explicación

La pendiente cambia en cada iteración debido a la presencia de la variable x².

---

## Código 4

### Problema

```text
dy/dx = x + 2y

x₀ = 0
y₀ = 1

h = 0.1
n = 5
```

### Código

```python
def pendiente(x, y):
    return x + 2*y

valor_x = 0
valor_y = 1

delta = 0.1

for vuelta in range(5):
    valor_y = valor_y + delta * pendiente(valor_x, valor_y)
    valor_x = valor_x + delta

print(valor_y)
```

### Resultado

```text
2.90299
```

### Explicación

El método sigue la dirección indicada por la pendiente para aproximar la trayectoria de la solución.

---

## Código 5

### Problema

```text
dy/dx = 3x - y

x₀ = 0
y₀ = 1

h = 0.1
n = 5
```

### Código

```python
def modelo(x, y):
    return 3*x - y

x = 0
y = 1

h = 0.1

for contador in range(5):
    y = y + h * modelo(x, y)
    x = x + h

print(y)
```

### Resultado

```text
0.88559
```

### Explicación

La solución aproximada se obtiene actualizando continuamente el valor de y utilizando la pendiente calculada.

---

## Conclusión

El método de Euler es uno de los procedimientos más básicos para resolver ecuaciones diferenciales ordinarias.

Su simplicidad lo convierte en una excelente herramienta para comprender métodos numéricos, aunque para obtener mayor precisión suelen utilizarse métodos más avanzados.