# Tema 4: Diferenciación e Integración Numérica

---

# Descripción General

La diferenciación e integración numérica reúne técnicas que permiten aproximar derivadas e integrales cuando obtener una solución exacta resulta complicado.

Estos métodos son ampliamente utilizados en áreas como ingeniería, ciencias computacionales, física y matemáticas aplicadas para analizar funciones y resolver problemas reales.

---

# Contenido

- Método del Trapecio
- Regla de Simpson 1/3
- Regla de Simpson 3/8
- Método de los Tres Puntos

---

# Método del Trapecio

El método del trapecio aproxima el área bajo una curva utilizando segmentos rectos que forman trapecios.

## Fórmula

:contentReference[oaicite:0]{index=0}

## Código

```python
expresion = input("Escribe la función usando x: ")

def funcion(x):
    return eval(expresion)

limite_inferior = float(input("Límite inferior: "))
limite_superior = float(input("Límite superior: "))

area = (
    (limite_superior - limite_inferior) / 2
) * (
    funcion(limite_inferior)
    + funcion(limite_superior)
)

print("Área aproximada:", area)
```

## Ejemplo de entrada

```text
x**2 + 2

0

4
```

## Observaciones

- Utiliza `x` como variable.
- Puede evaluarse cualquier función válida de Python.
- Es uno de los métodos de integración más sencillos.

---

# Regla de Simpson 1/3

La regla de Simpson 1/3 aproxima integrales utilizando una parábola que pasa por tres puntos.

## Fórmula

:contentReference[oaicite:1]{index=1}

## Código

```python
funcion_texto = input("Ingresa la función: ")

def evaluar(x):
    return eval(funcion_texto)

inicio = float(input("Valor inicial: "))
fin = float(input("Valor final: "))

medio = (inicio + fin) / 2

resultado = (
    (fin - inicio) / 6
) * (
    evaluar(inicio)
    + 4 * evaluar(medio)
    + evaluar(fin)
)

print("Integral aproximada:", resultado)
```

## Ejemplo de entrada

```text
x**3 + x

0

4
```

## Observaciones

- Utiliza tres evaluaciones de la función.
- Generalmente es más preciso que el método del trapecio.
- Funciona mejor con funciones suaves.

---

# Regla de Simpson 3/8

Este método emplea una aproximación basada en polinomios cúbicos y divide el intervalo en tres partes iguales.

## Fórmula

:contentReference[oaicite:2]{index=2}

## Código

```python
texto = input("Introduce la función: ")

def f(x):
    return eval(texto)

a = float(input("Valor inicial: "))
b = float(input("Valor final: "))

h = (b - a) / 3

p0 = a
p1 = a + h
p2 = a + 2*h
p3 = b

aproximacion = (
    3 * h / 8
) * (
    f(p0)
    + 3 * f(p1)
    + 3 * f(p2)
    + f(p3)
)

print("Resultado:", aproximacion)
```

## Ejemplo de entrada

```text
x**2 + 1

0

6
```

## Observaciones

- Divide automáticamente el intervalo.
- Utiliza cuatro puntos de evaluación.
- Suele ofrecer buena precisión para funciones continuas.

---

# Método de los Tres Puntos

El método de los tres puntos permite aproximar derivadas utilizando diferencias centrales.

## Fórmula

:contentReference[oaicite:3]{index=3}

## Código

```python
funcion_usuario = input("Escribe la función: ")

def calcular(x):
    return eval(funcion_usuario)

punto = float(input("Punto a evaluar: "))
incremento = float(input("Valor de h: "))

derivada = (
    calcular(punto + incremento)
    - calcular(punto - incremento)
) / (
    2 * incremento
)

print("Derivada aproximada:", derivada)
```

## Ejemplo de entrada

```text
x**3 + 2*x

2

0.01
```

## Observaciones

- Utiliza diferencias centrales.
- Valores pequeños de `h` suelen mejorar la precisión.
- Es útil cuando la derivada exacta no se conoce.

---

# Conclusión

Los métodos de diferenciación e integración numérica permiten obtener aproximaciones confiables de derivadas e integrales.

Cada técnica posee características distintas en precisión y complejidad, por lo que la elección depende del problema que se desea resolver.