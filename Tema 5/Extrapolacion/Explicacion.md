# Tema 4: Diferenciación e Integración Numérica

## Subtema: Extrapolación Externa

---

## Descripción

La extrapolación externa es un método utilizado para estimar valores que se encuentran fuera del intervalo de datos conocidos.

A partir de dos puntos conocidos se construye una recta y se utiliza para predecir valores más allá del rango original.

---

## Código 1

### Datos

```text
(2,4)
(5,10)

x = 7
```

### Código

```python
x_inicial = 2
y_inicial = 4

x_final = 5
y_final = 10

valor_buscado = 7

estimacion = y_inicial + (
    (y_final - y_inicial) /
    (x_final - x_inicial)
) * (valor_buscado - x_inicial)

print(estimacion)
```

### Resultado

```text
14.0
```

### Explicación

El valor calculado se encuentra fuera del intervalo original, por lo que corresponde a una extrapolación.

---

## Código 2

### Datos

```text
(1,3)
(4,12)

x = 6
```

### Código

```python
x1 = 1
y1 = 3

x2 = 4
y2 = 12

objetivo = 6

resultado = y1 + (
    (y2 - y1) /
    (x2 - x1)
) * (objetivo - x1)

print(resultado)
```

### Resultado

```text
18.0
```

### Explicación

La pendiente de la recta se utiliza para extender el comportamiento de los datos conocidos.

---

## Código 3

### Datos

```text
(0,2)
(4,14)

x = 6
```

### Código

```python
dato_x1 = 0
dato_y1 = 2

dato_x2 = 4
dato_y2 = 14

nuevo_x = 6

nuevo_y = dato_y1 + (
    (dato_y2 - dato_y1) /
    (dato_x2 - dato_x1)
) * (nuevo_x - dato_x1)

print(nuevo_y)
```

### Resultado

```text
20.0
```

### Explicación

La extrapolación permite estimar valores más allá de los datos disponibles.

---

## Código 4

### Datos

```text
(3,8)
(8,18)

x = 10
```

### Código

```python
a = 3
b = 8

c = 8
d = 18

valor = 10

aproximacion = b + (
    (d - b) /
    (c - a)
) * (valor - a)

print(aproximacion)
```

### Resultado

```text
22.0
```

### Explicación

La estimación se obtiene prolongando la línea formada por los puntos conocidos.

---

## Código 5

### Datos

```text
(2,7)
(6,19)

x = 9
```

### Código

```python
x0 = 2
y0 = 7

x1 = 6
y1 = 19

x = 9

valor_estimado = y0 + (
    (y1 - y0) /
    (x1 - x0)
) * (x - x0)

print(valor_estimado)
```

### Resultado

```text
28.0
```

### Explicación

Se utiliza una relación lineal para calcular un valor situado fuera del intervalo conocido.

---

## Conclusión

La extrapolación externa permite predecir valores que se encuentran fuera del rango de datos disponibles.

Aunque es una herramienta útil para realizar estimaciones, la precisión disminuye mientras más lejos se encuentre el valor extrapolado del intervalo original.