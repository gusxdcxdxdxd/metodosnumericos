# Tema 5: Interpolación y Ajuste de Funciones

## Subtema: Interpolación Segmentada

---

## Descripción

La interpolación segmentada consiste en dividir los datos en intervalos y aplicar una interpolación lineal diferente en cada segmento.

Este método es útil cuando los datos presentan cambios de comportamiento y una sola recta no representa adecuadamente toda la información.

---

## Código 1

### Datos

```text
(0,2)
(2,6)
(4,10)

x = 3
```

### Código

```python
valor = 3

if valor <= 2:

    resultado = 2 + (
        (6 - 2) / (2 - 0)
    ) * (valor - 0)

else:

    resultado = 6 + (
        (10 - 6) / (4 - 2)
    ) * (valor - 2)

print(resultado)
```

### Resultado

```text
8.0
```

### Explicación

Como el valor se encuentra entre 2 y 4, se utiliza el segundo segmento lineal.

---

## Código 2

### Datos

```text
(1,3)
(3,9)
(5,15)

x = 4
```

### Código

```python
x = 4

if x <= 3:

    y = 3 + (
        (9 - 3) / (3 - 1)
    ) * (x - 1)

else:

    y = 9 + (
        (15 - 9) / (5 - 3)
    ) * (x - 3)

print(y)
```

### Resultado

```text
12.0
```

### Explicación

La interpolación se realiza utilizando únicamente el intervalo donde se encuentra el dato buscado.

---

## Código 3

### Datos

```text
(2,5)
(4,13)
(6,21)

x = 5
```

### Código

```python
dato = 5

if dato <= 4:

    valor = 5 + (
        (13 - 5) / (4 - 2)
    ) * (dato - 2)

else:

    valor = 13 + (
        (21 - 13) / (6 - 4)
    ) * (dato - 4)

print(valor)
```

### Resultado

```text
17.0
```

### Explicación

Cada tramo posee su propia pendiente, permitiendo representar mejor los datos.

---

## Código 4

### Datos

```text
(0,1)
(3,7)
(6,19)

x = 4
```

### Código

```python
numero = 4

if numero <= 3:

    respuesta = 1 + (
        (7 - 1) / (3 - 0)
    ) * (numero - 0)

else:

    respuesta = 7 + (
        (19 - 7) / (6 - 3)
    ) * (numero - 3)

print(respuesta)
```

### Resultado

```text
11.0
```

### Explicación

El valor buscado se obtiene utilizando el segmento correspondiente al intervalo donde se encuentra.

---

## Código 5

### Datos

```text
(1,4)
(3,10)
(5,22)

x = 4
```

### Código

```python
objetivo = 4

if objetivo <= 3:

    resultado = 4 + (
        (10 - 4) / (3 - 1)
    ) * (objetivo - 1)

else:

    resultado = 10 + (
        (22 - 10) / (5 - 3)
    ) * (objetivo - 3)

print(resultado)
```

### Resultado

```text
16.0
```

### Explicación

La interpolación segmentada permite ajustar diferentes rectas a distintos intervalos de datos.

---

## Conclusión

La interpolación segmentada mejora las estimaciones cuando los datos presentan comportamientos distintos en diferentes regiones.

Al trabajar por intervalos, suele proporcionar resultados más representativos que una única interpolación aplicada a todo el conjunto de datos.