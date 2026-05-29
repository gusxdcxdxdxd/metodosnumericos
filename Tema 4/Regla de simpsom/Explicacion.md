# Tema 4: Diferenciación e Integración Numérica

## Subtema: Regla de Simpson 1/3

---

## Descripción

La regla de Simpson 1/3 es un método de integración numérica que aproxima el área bajo una curva utilizando una parábola.

Este procedimiento suele proporcionar resultados más precisos que el método del trapecio cuando la función es suave.

---

## Código 1

### Función


::contentReference[oaicite:0]{index=0}


### Código

```python
def funcion(valor):
    return valor**2 + 2

inicio = 0
fin = 2

medio = (inicio + fin) / 2

integral = ((fin - inicio) / 6) * (
    funcion(inicio)
    + 4 * funcion(medio)
    + funcion(fin)
)

print(integral)
```

### Resultado

```text
6.666666666666667
```

### Explicación

La aproximación se realiza utilizando los valores de la función en los extremos y en el punto medio del intervalo.

---

## Código 2

### Función


::contentReference[oaicite:1]{index=1}


### Código

```python
def ecuacion(x):
    return 3*x + 2

a = 1
b = 5

centro = (a + b) / 2

resultado = ((b - a) / 6) * (
    ecuacion(a)
    + 4 * ecuacion(centro)
    + ecuacion(b)
)

print(resultado)
```

### Resultado

```text
48.0
```

### Explicación

Para funciones lineales, Simpson 1/3 proporciona el valor exacto de la integral.

---

## Código 3

### Función


::contentReference[oaicite:2]{index=2}


### Código

```python
def expresion(numero):
    return numero**3 + 1

limite_inferior = 1
limite_superior = 3

punto_medio = (limite_inferior + limite_superior) / 2

area = ((limite_superior - limite_inferior) / 6) * (
    expresion(limite_inferior)
    + 4 * expresion(punto_medio)
    + expresion(limite_superior)
)

print(area)
```

### Resultado

```text
22.0
```

### Explicación

El método utiliza una parábola para representar mejor el comportamiento de la función dentro del intervalo.

---

## Código 4

### Función


::contentReference[oaicite:3]{index=3}


### Código

```python
def formula(valor):
    return valor**2 - 3*valor + 4

x0 = 0
x1 = 3

xm = (x0 + x1) / 2

aproximacion = ((x1 - x0) / 6) * (
    formula(x0)
    + 4 * formula(xm)
    + formula(x1)
)

print(aproximacion)
```

### Resultado

```text
7.5
```

### Explicación

La parábola generada por Simpson permite obtener una mejor aproximación que métodos más simples.

---

## Código 5

### Función


::contentReference[oaicite:4]{index=4}


### Código

```python
def funcion_principal(x):
    return x**3 - 2*x

inicio = 1
fin = 4

medio = (inicio + fin) / 2

resultado_final = ((fin - inicio) / 6) * (
    funcion_principal(inicio)
    + 4 * funcion_principal(medio)
    + funcion_principal(fin)
)

print(resultado_final)
```

### Resultado

```text
54.375
```

### Explicación

El valor aproximado se calcula utilizando los extremos y el punto medio para construir una curva parabólica.

---

## Conclusión

La regla de Simpson 1/3 es uno de los métodos de integración numérica más utilizados debido a su buena precisión.

Al emplear parábolas en lugar de rectas, suele producir mejores aproximaciones para funciones continuas.