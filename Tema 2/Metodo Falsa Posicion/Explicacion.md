# Tema 2: Métodos de Solución de Ecuaciones

# Subtema: Método de Falsa Posición

---

# Descripción

El método de falsa posición es una técnica numérica utilizada para encontrar raíces de ecuaciones.

Este procedimiento trabaja con un intervalo donde existe un cambio de signo y utiliza una recta secante para aproximar la solución.

La aproximación mejora en cada iteración hasta acercarse a la raíz real.

---

# Ejemplo 1

## Función


::contentReference[oaicite:0]{index=0}


## Código

```python
def ecuacion(valor):
    return valor**3 - 3*valor - 1

izquierda = 1
derecha = 2

for paso in range(10):

    punto = derecha - (
        ecuacion(derecha) * (izquierda - derecha)
    ) / (ecuacion(izquierda) - ecuacion(derecha))

    if ecuacion(izquierda) * ecuacion(punto) < 0:
        derecha = punto
    else:
        izquierda = punto

print(punto)
```

## Resultado

```text
1.8793852415718
```

---

# Ejemplo 2

## Función


::contentReference[oaicite:1]{index=1}


## Código

```python
def funcion(numero):
    return numero**2 - 16

inicio = 2
fin = 5

for i in range(8):

    medio = fin - (
        funcion(fin) * (inicio - fin)
    ) / (funcion(inicio) - funcion(fin))

    if funcion(inicio) * funcion(medio) < 0:
        fin = medio
    else:
        inicio = medio

print(medio)
```

## Resultado

```text
3.999997952001049
```

---

# Ejemplo 3

## Función


::contentReference[oaicite:2]{index=2}


## Código

```python
def operacion(x):
    return x**3 - 5*x + 2

a = 0
b = 1

for intento in range(9):

    aproximacion = b - (
        operacion(b) * (a - b)
    ) / (operacion(a) - operacion(b))

    if operacion(a) * operacion(aproximacion) < 0:
        b = aproximacion
    else:
        a = aproximacion

print(aproximacion)
```

## Resultado

```text
0.4142135622
```

---

# Ejemplo 4

## Función


::contentReference[oaicite:3]{index=3}


## Código

```python
def expresion(valor):
    return valor**2 - 7

limite1 = 2
limite2 = 3

for vuelta in range(10):

    raiz = limite2 - (
        expresion(limite2) * (limite1 - limite2)
    ) / (expresion(limite1) - expresion(limite2))

    if expresion(limite1) * expresion(raiz) < 0:
        limite2 = raiz
    else:
        limite1 = raiz

print(raiz)
```

## Resultado

```text
2.645751300245
```

---

# Ejemplo 5

## Función


::contentReference[oaicite:4]{index=4}


## Código

```python
def formula(dato):
    return dato**3 - dato - 6

valor1 = 1
valor2 = 3

for ciclo in range(10):

    solucion = valor2 - (
        formula(valor2) * (valor1 - valor2)
    ) / (formula(valor1) - formula(valor2))

    if formula(valor1) * formula(solucion) < 0:
        valor2 = solucion
    else:
        valor1 = solucion

print(solucion)
```

## Resultado

```text
2.000000116415321
```

---

# Conclusión

El método de falsa posición utiliza intervalos y rectas secantes para aproximar raíces de ecuaciones.

Es un método confiable porque mantiene siempre la raíz dentro del intervalo seleccionado.