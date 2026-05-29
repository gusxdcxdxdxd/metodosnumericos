# Tema 5: Interpolación y Ajuste de Funciones

## Subtema: Interpolación Lineal

---

## Descripción

La interpolación lineal es un método numérico utilizado para estimar valores que se encuentran entre dos puntos conocidos.

Este procedimiento supone que el comportamiento entre los puntos puede aproximarse mediante una línea recta.

---

## Código 1

### Datos

```text
(2,4)
(6,12)

x = 4
```

### Código

```python
x_inicial = 2
y_inicial = 4

x_final = 6
y_final = 12

valor = 4

resultado = y_inicial + (
    (y_final - y_inicial)
    / (x_final - x_inicial)
) * (valor - x_inicial)

print(resultado)
```

### Resultado

```text
8.0
```

### Explicación

El valor calculado se encuentra dentro del intervalo definido por los dos puntos conocidos.

---

## Código 2

### Datos

```text
(1,3)
(5,15)

x = 3
```

### Código

```python
a = 1
b = 3

c = 5
d = 15

x = 3

estimacion = b + (
    (d - b)
    / (c - a)
) * (x - a)

print(estimacion)
```

### Resultado

```text
9.0
```

### Explicación

La interpolación genera un valor intermedio siguiendo la tendencia lineal de los datos.

---

## Código 3

### Datos

```text
(0,2)
(8,18)

x = 5
```

### Código

```python
x0 = 0
y0 = 2

x1 = 8
y1 = 18

punto = 5

valor_interpolado = y0 + (
    (y1 - y0)
    / (x1 - x0)
) * (punto - x0)

print(valor_interpolado)
```

### Resultado

```text
12.0
```

### Explicación

El resultado corresponde a una aproximación obtenida entre los dos valores conocidos.

---

## Código 4

### Datos

```text
(3,7)
(9,25)

x = 6
```

### Código

```python
inicio_x = 3
inicio_y = 7

fin_x = 9
fin_y = 25

objetivo = 6

respuesta = inicio_y + (
    (fin_y - inicio_y)
    / (fin_x - inicio_x)
) * (objetivo - inicio_x)

print(respuesta)
```

### Resultado

```text
16.0
```

### Explicación

La pendiente obtenida entre los dos puntos permite estimar valores intermedios.

---

## Código 5

### Datos

```text
(2,6)
(7,21)

x = 4
```

### Código

```python
dato_x1 = 2
dato_y1 = 6

dato_x2 = 7
dato_y2 = 21

valor_x = 4

valor_y = dato_y1 + (
    (dato_y2 - dato_y1)
    / (dato_x2 - dato_x1)
) * (valor_x - dato_x1)

print(valor_y)
```

### Resultado

```text
12.0
```

### Explicación

La interpolación lineal permite obtener estimaciones rápidas cuando se conocen dos puntos cercanos.

---

## Conclusión

La interpolación lineal es una herramienta sencilla y eficiente para estimar valores dentro de un intervalo conocido.

Su principal ventaja es la facilidad de implementación y comprensión, aunque su precisión depende de que la relación entre los datos sea aproximadamente lineal.