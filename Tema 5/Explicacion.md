# Tema 5: Interpolación y Ajuste de Funciones

---

# Descripción General

La interpolación y el ajuste de funciones son técnicas numéricas que permiten estimar valores a partir de información previamente conocida.

Estas herramientas son ampliamente utilizadas en ingeniería, ciencias computacionales, estadística y análisis de datos para realizar aproximaciones cuando no se dispone de todos los valores necesarios.

La interpolación se utiliza para estimar datos dentro de un intervalo conocido, mientras que la extrapolación permite realizar predicciones fuera de dicho intervalo.

---

# Contenido

- Interpolación Lineal
- Interpolación Cuadrática
- Interpolación Segmentada
- Extrapolación Externa

---

# Interpolación Lineal

La interpolación lineal utiliza dos puntos conocidos para estimar un valor intermedio suponiendo que la relación entre ellos puede representarse mediante una línea recta.

## Fórmula

:contentReference[oaicite:0]{index=0}

## Código

```python
x_inicio = float(input("Valor de x inicial: "))
y_inicio = float(input("Valor de y inicial: "))

x_final = float(input("Valor de x final: "))
y_final = float(input("Valor de y final: "))

objetivo = float(input("Valor a estimar: "))

resultado = y_inicio + (
    (y_final - y_inicio) /
    (x_final - x_inicio)
) * (objetivo - x_inicio)

print("Valor interpolado:", resultado)
```

## Observaciones

- Utiliza únicamente dos puntos.
- El valor buscado debe encontrarse dentro del intervalo.
- Es el método de interpolación más sencillo.

---

# Interpolación Cuadrática

La interpolación cuadrática utiliza tres puntos conocidos para construir una parábola que permita estimar valores intermedios.

## Código

```python
def interpolacion(valor):

    x0 = float(input("x0: "))
    y0 = float(input("y0: "))

    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    termino_a = y0 * (
        (valor - x1) * (valor - x2)
    ) / (
        (x0 - x1) * (x0 - x2)
    )

    termino_b = y1 * (
        (valor - x0) * (valor - x2)
    ) / (
        (x1 - x0) * (x1 - x2)
    )

    termino_c = y2 * (
        (valor - x0) * (valor - x1)
    ) / (
        (x2 - x0) * (x2 - x1)
    )

    return termino_a + termino_b + termino_c

punto = float(input("Valor a calcular: "))

print("Resultado:", interpolacion(punto))
```

## Observaciones

- Utiliza tres puntos conocidos.
- Emplea el polinomio de Lagrange.
- Puede representar comportamientos curvos de los datos.

---

# Interpolación Segmentada

La interpolación segmentada divide los datos en diferentes intervalos y aplica interpolación lineal en el segmento adecuado.

## Código

```python
xa = float(input("xa: "))
ya = float(input("ya: "))

xb = float(input("xb: "))
yb = float(input("yb: "))

xc = float(input("xc: "))
yc = float(input("yc: "))

valor = float(input("Valor a interpolar: "))

if valor <= xb:

    resultado = ya + (
        (yb - ya) /
        (xb - xa)
    ) * (valor - xa)

else:

    resultado = yb + (
        (yc - yb) /
        (xc - xb)
    ) * (valor - xb)

print("Resultado:", resultado)
```

## Observaciones

- Permite trabajar con varios intervalos.
- Selecciona automáticamente el segmento correcto.
- Mejora la representación de conjuntos de datos extensos.

---

# Extrapolación Externa

La extrapolación externa estima valores localizados fuera del rango de datos disponibles.

## Fórmula

:contentReference[oaicite:1]{index=1}

## Código

```python
x0 = float(input("Primer valor de x: "))
y0 = float(input("Primer valor de y: "))

x1 = float(input("Segundo valor de x: "))
y1 = float(input("Segundo valor de y: "))

x = float(input("Valor a extrapolar: "))

estimacion = y0 + (
    (y1 - y0) /
    (x1 - x0)
) * (x - x0)

print("Valor estimado:", estimacion)
```

## Observaciones

- El valor buscado debe encontrarse fuera del intervalo.
- Utiliza una tendencia lineal para realizar la predicción.
- La precisión disminuye cuanto más lejos esté el valor extrapolado.

---

# Conclusión

Los métodos de interpolación y extrapolación permiten estimar valores desconocidos utilizando información disponible.

La elección del método depende de la cantidad de datos conocidos, del comportamiento de la función y de la precisión requerida para el problema que se desea resolver.