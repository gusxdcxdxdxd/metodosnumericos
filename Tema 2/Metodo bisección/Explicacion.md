# Tema 2: Métodos de Solución de Ecuaciones
## Subtema: Método de Bisección

---

## Descripción

El método de bisección consiste en dividir repetidamente un intervalo en dos partes iguales hasta aproximarse a la raíz de una función.

Este método requiere que exista cambio de signo en el intervalo.

---

## Código 1

### Función

f(x)=x³-x-2

### Código

```python
def f(x):
    return x**3 - x - 2

a = 1
b = 2

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)
```

### Resultado

1.5205078125

---

## Código 2

### Función

f(x)=x²-4

### Código

```python
def f(x):
    return x**2 - 4

a = 0
b = 3

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)
```

### Resultado

2.0009765625

---

## Código 3

### Función

f(x)=x³-4x-9

### Código

```python
def f(x):
    return x**3 - 4*x - 9

a = 2
b = 3

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)
```

### Resultado

2.70654296875

---

## Código 4

### Función

f(x)=x²-2

### Código

```python
def f(x):
    return x**2 - 2

a = 1
b = 2

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)
```

### Resultado

1.4150390625

---

## Código 5

### Función

f(x)=x³-2x-5

### Código

```python
def f(x):
    return x**3 - 2*x - 5

a = 2
b = 3

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)
```

### Resultado

2.0947265625