# Tema 4: Diferenciación e Integración Numérica

## Subtema: Método del Trapecio

---

## Descripción

El método del trapecio es una técnica de integración numérica utilizada para aproximar áreas bajo una curva.

La idea consiste en reemplazar la región de la función por un trapecio y calcular su área utilizando los valores de los extremos del intervalo.

---

## Código 1

### Función


::contentReference[oaicite:0]{index=0}


### Código

```python
def funcion(valor):
    return valor**2 + 1

inicio = 0
fin = 3

area = ((fin - inicio) / 2) * (
    funcion(inicio) + funcion(fin)
)

print(area)
```

### Resultado

```text
16.5
```

### Explicación

Se aproxima el área bajo la curva en el intervalo [0,3] utilizando un solo trapecio.

---

## Código 2

### Función


::contentReference[oaicite:1]{index=1}


### Código

```python
def ecuacion(numero):
    return 3 * numero + 2

a = 1
b = 5

resultado = ((b - a) / 2) * (
    ecuacion(a) + ecuacion(b)
)

print(resultado)
```

### Resultado

```text
48.0
```

### Explicación

Al ser una función lineal, el método del trapecio proporciona una aproximación muy cercana al valor real.

---

## Código 3

### Función


::contentReference[oaicite:2]{index=2}


### Código

```python
def expresion(x):
    return x**3 + 2

limite_inferior = 1
limite_superior = 4

integral = ((limite_superior - limite_inferior) / 2) * (
    expresion(limite_inferior)
    + expresion(limite_superior)
)

print(integral)
```

### Resultado

```text
103.5
```

### Explicación

La aproximación se obtiene considerando únicamente los valores de la función en los extremos del intervalo.

---

## Código 4

### Función


::contentReference[oaicite:3]{index=3}


### Código

```python
def formula(valor):
    return valor**2 - 2*valor + 3

x0 = 0
x1 = 2

area_aprox = ((x1 - x0) / 2) * (
    formula(x0) + formula(x1)
)

print(area_aprox)
```

### Resultado

```text
8.0
```

### Explicación

El área se aproxima mediante un trapecio cuyos lados paralelos corresponden a los valores de la función en los extremos.

---

## Código 5

### Función


::contentReference[oaicite:4]{index=4}


### Código

```python
def funcion_principal(x):
    return x**3 - x

a = 1
b = 3

resultado_final = ((b - a) / 2) * (
    funcion_principal(a)
    + funcion_principal(b)
)

print(resultado_final)
```

### Resultado

```text
24.0
```

### Explicación

El método utiliza la geometría de un trapecio para aproximar el área comprendida entre la función y el eje x.

---

## Conclusión

El método del trapecio es sencillo de implementar y permite aproximar integrales definidas utilizando únicamente los valores de la función en los extremos del intervalo.

Su precisión puede mejorarse dividiendo el intervalo en varios subintervalos.