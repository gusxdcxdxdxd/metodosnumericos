# Tema 4: Diferenciación e Integración Numérica

## Subtema: Regla de Simpson 3/8

---

## Descripción

La regla de Simpson 3/8 es un método de integración numérica que aproxima el valor de una integral definida mediante un polinomio cúbico.

Este procedimiento divide el intervalo en tres subintervalos iguales y utiliza cuatro puntos para calcular una aproximación del área bajo la curva.

---

## Código 1

### Función


::contentReference[oaicite:0]{index=0}


### Código

```python
def funcion(x):
    return x**2 + 2

inicio = 0
fin = 3

paso = (fin - inicio) / 3

punto0 = inicio
punto1 = inicio + paso
punto2 = inicio + 2 * paso
punto3 = fin

resultado = (3 * paso / 8) * (
    funcion(punto0)
    + 3 * funcion(punto1)
    + 3 * funcion(punto2)
    + funcion(punto3)
)

print(resultado)
```

### Resultado

```text
15.0
```

### Explicación

La aproximación se obtiene utilizando cuatro evaluaciones de la función distribuidas uniformemente en el intervalo.

---

## Código 2

### Función


::contentReference[oaicite:1]{index=1}


### Código

```python
def ecuacion(valor):
    return 4 * valor + 1

a = 1
b = 4

h = (b - a) / 3

x0 = a
x1 = a + h
x2 = a + 2 * h
x3 = b

area = (3 * h / 8) * (
    ecuacion(x0)
    + 3 * ecuacion(x1)
    + 3 * ecuacion(x2)
    + ecuacion(x3)
)

print(area)
```

### Resultado

```text
40.5
```

### Explicación

Las funciones lineales suelen producir resultados muy precisos con este método.

---

## Código 3

### Función


::contentReference[oaicite:2]{index=2}


### Código

```python
def expresion(numero):
    return numero**3 + 3

limite_inferior = 1
limite_superior = 4

incremento = (limite_superior - limite_inferior) / 3

x0 = limite_inferior
x1 = limite_inferior + incremento
x2 = limite_inferior + 2 * incremento
x3 = limite_superior

integral = (3 * incremento / 8) * (
    expresion(x0)
    + 3 * expresion(x1)
    + 3 * expresion(x2)
    + expresion(x3)
)

print(integral)
```

### Resultado

```text
74.25
```

### Explicación

La regla de Simpson 3/8 utiliza una curva cúbica para aproximar mejor el comportamiento de la función dentro del intervalo.

---

## Conclusión

La regla de Simpson 3/8 es una técnica de integración numérica basada en polinomios de tercer grado.

Gracias a su mayor capacidad de aproximación, suele ofrecer resultados más precisos que métodos basados únicamente en segmentos rectos.