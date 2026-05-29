# Tema 4: Diferenciación e Integración Numérica

## Subtema: Método de los Tres Puntos

---

## Descripción

El método de los tres puntos es una técnica de diferenciación numérica que permite aproximar la derivada de una función utilizando valores cercanos al punto de interés.

Este procedimiento emplea un punto anterior, el punto central y un punto posterior para estimar la pendiente de la función.

---

## Código 1

### Función


::contentReference[oaicite:0]{index=0}


### Código

```python
def funcion(valor):
    return valor**2 + 3*valor

punto = 2
incremento = 0.1

derivada = (
    funcion(punto + incremento)
    - funcion(punto - incremento)
) / (2 * incremento)

print(derivada)
```

### Resultado

```text
7.0
```

### Explicación

La derivada exacta de la función es:

```text
2x + 3
```

Al evaluar en x = 2 se obtiene un valor cercano a 7.

---

## Código 2

### Función


::contentReference[oaicite:1]{index=1}


### Código

```python
def ecuacion(numero):
    return 4 * numero - 5

x0 = 1
paso = 0.05

resultado = (
    ecuacion(x0 + paso)
    - ecuacion(x0 - paso)
) / (2 * paso)

print(resultado)
```

### Resultado

```text
4.0
```

### Explicación

La pendiente de una función lineal es constante, por lo que la aproximación coincide con la derivada real.

---

## Código 3

### Función


::contentReference[oaicite:2]{index=2}


### Código

```python
def expresion(x):
    return x**3 + 2*x

valor = 2
h = 0.1

aproximacion = (
    expresion(valor + h)
    - expresion(valor - h)
) / (2 * h)

print(aproximacion)
```

### Resultado

```text
14.01
```

### Explicación

La derivada exacta es:

```text
3x² + 2
```

Para x = 2 el resultado esperado es 14.

---

## Código 4

### Función


::contentReference[oaicite:3]{index=3}


### Código

```python
def formula(dato):
    return dato**2 - 4*dato + 1

centro = 3
delta = 0.1

respuesta = (
    formula(centro + delta)
    - formula(centro - delta)
) / (2 * delta)

print(respuesta)
```

### Resultado

```text
2.0
```

### Explicación

La derivada analítica es:

```text
2x - 4
```

Al evaluar en x = 3 se obtiene exactamente 2.

---

## Código 5

### Función


::contentReference[oaicite:4]{index=4}


### Código

```python
def funcion_principal(x):
    return x**3 - x

punto = 1.5
incremento = 0.1

valor_derivada = (
    funcion_principal(punto + incremento)
    - funcion_principal(punto - incremento)
) / (2 * incremento)

print(valor_derivada)
```

### Resultado

```text
5.76
```

### Explicación

La derivada exacta es:

```text
3x² - 1
```

En x = 1.5 el valor teórico es 5.75, muy cercano a la aproximación obtenida.

---

## Conclusión

El método de los tres puntos permite aproximar derivadas utilizando información cercana al punto de evaluación.

Mientras más pequeño sea el valor de h, normalmente se obtiene una aproximación más precisa de la derivada real.