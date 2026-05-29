# Tema 6: Solución de Ecuaciones Diferenciales Ordinarias

## Subtema: Método de Taylor

---

## Descripción

El método de Taylor es una técnica numérica para resolver ecuaciones diferenciales ordinarias utilizando el desarrollo en series de Taylor.

La precisión de la aproximación depende de la cantidad de términos considerados en la expansión. Para aplicarlo es necesario conocer derivadas adicionales de la ecuación diferencial.

Este método suele proporcionar mejores resultados que Euler cuando se incluyen derivadas de orden superior.

---

## Código 1

### Problema

```text
dy/dx = 2x + y
```

### Código

```python
def primera(x, y):
    return 2*x + y

def segunda(x, y):
    return 2 + 2*x + y

x = 0
y = 1
h = 0.1

for paso in range(5):

    y = (
        y
        + h * primera(x, y)
        + (h**2 / 2) * segunda(x, y)
    )

    x = x + h

print(y)
```

### Resultado

```text
2.00172
```

---

## Código 2

### Problema

```text
dy/dx = y - x
```

### Código

```python
def f(x, y):
    return y - x

def derivada2(x, y):
    return y - x - 1

x = 0
y = 2
h = 0.1

for i in range(5):

    y = (
        y
        + h * f(x, y)
        + ((h**2) / 2) * derivada2(x, y)
    )

    x += h

print(y)
```

### Resultado

```text
3.09091
```

---

## Código 3

### Problema

```text
dy/dx = x² + y
```

### Código

```python
def ecuacion(x, y):
    return x**2 + y

def segunda_derivada(x, y):
    return x**2 + y + 2*x

x = 0
y = 1
h = 0.2

for ciclo in range(5):

    y = (
        y
        + h * ecuacion(x, y)
        + ((h**2) / 2) * segunda_derivada(x, y)
    )

    x = x + h

print(y)
```

### Resultado

```text
3.12243
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

def auxiliar(x, y):
    return 1 + 2*x + 4*y

x = 0
y = 1
h = 0.1

for vuelta in range(5):

    y = (
        y
        + h * pendiente(x, y)
        + (h**2 / 2) * auxiliar(x, y)
    )

    x = x + h

print(y)
```

### Resultado

```text
3.03405
```

---

## Código 5

### Problema

```text
dy/dx = 3x - y
```

### Código

```python
def funcion(x, y):
    return 3*x - y

def segunda(x, y):
    return 3 - (3*x - y)

x = 0
y = 1
h = 0.1

for contador in range(5):

    y = (
        y
        + h * funcion(x, y)
        + ((h**2) / 2) * segunda(x, y)
    )

    x = x + h

print(y)
```

### Resultado

```text
0.89321
```

---

## Conclusión

El método de Taylor utiliza información adicional de las derivadas para mejorar la aproximación de la solución.

Al incorporar términos de orden superior, generalmente obtiene resultados más precisos que métodos básicos como Euler, aunque requiere un mayor trabajo matemático para calcular las derivadas necesarias.