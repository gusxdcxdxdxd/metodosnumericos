# Tema 2: Métodos Numéricos para Resolver Ecuaciones

---

# Introducción

Los métodos numéricos de solución de ecuaciones permiten encontrar raíces aproximadas de funciones matemáticas.

Una raíz corresponde al valor donde:

:contentReference[oaicite:0]{index=0}

Estos métodos son utilizados cuando resolver una ecuación de forma exacta resulta complicado o imposible mediante métodos algebraicos tradicionales.

Cada procedimiento genera aproximaciones sucesivas hasta acercarse al resultado deseado.

---

# Contenido

- Método de Bisección
- Método de Falsa Posición
- Método de la Secante
- Método de Newton-Raphson

---

# Método de Bisección

Este método divide continuamente un intervalo en dos partes iguales.

Después selecciona el subintervalo donde existe cambio de signo para seguir aproximando la raíz.

## Fórmula

:contentReference[oaicite:1]{index=1}

## Programa

```python
def ecuacion(x):
    return x**3 - 5   # modifica la función

izquierda = float(input("Límite izquierdo: "))
derecha = float(input("Límite derecho: "))
error = float(input("Tolerancia: "))

while (derecha - izquierda)/2 > error:

    punto_medio = (izquierda + derecha) / 2

    if ecuacion(izquierda) * ecuacion(punto_medio) < 0:
        derecha = punto_medio
    else:
        izquierda = punto_medio

print("Resultado aproximado:", punto_medio)
```

## Observaciones

- Cambia la ecuación dentro de `ecuacion(x)`
- El intervalo debe contener cambio de signo
- La función debe ser continua

---

# Método de Falsa Posición

La falsa posición utiliza una recta secante para calcular aproximaciones más cercanas a la raíz.

## Fórmula

:contentReference[oaicite:2]{index=2}

## Programa

```python
def funcion(x):
    return x**3 - 7   # modifica la función

inicio = float(input("Valor inicial: "))
fin = float(input("Valor final: "))
tolerancia = float(input("Tolerancia: "))

aprox = inicio

while True:

    anterior = aprox

    aprox = fin - (
        funcion(fin) * (inicio - fin)
    ) / (funcion(inicio) - funcion(fin))

    if abs(aprox - anterior) < tolerancia:
        break

    if funcion(inicio) * funcion(aprox) < 0:
        fin = aprox
    else:
        inicio = aprox

print("Raíz aproximada:", aprox)
```

## Observaciones

- Debe existir cambio de signo
- La función puede modificarse fácilmente
- Generalmente converge más rápido que bisección

---

# Método de la Secante

La secante utiliza dos valores iniciales para construir nuevas aproximaciones sin usar derivadas.

## Fórmula

:contentReference[oaicite:3]{index=3}

## Programa

```python
def expresion(x):
    return x**2 - 6   # modifica función

valor1 = float(input("Primer valor: "))
valor2 = float(input("Segundo valor: "))
margen = float(input("Tolerancia: "))

while True:

    nuevo = valor2 - (
        expresion(valor2) * (valor2 - valor1)
    ) / (
        expresion(valor2) - expresion(valor1)
    )

    if abs(nuevo - valor2) < margen:
        break

    valor1 = valor2
    valor2 = nuevo

print("Resultado:", nuevo)
```

## Observaciones

- No necesita derivadas
- Los valores iniciales pueden cambiarse
- Suele converger rápidamente

---

# Método de Newton-Raphson

Newton-Raphson utiliza derivadas para generar aproximaciones muy precisas en pocas iteraciones.

## Fórmula

:contentReference[oaicite:4]{index=4}

## Programa

```python
def formula(x):
    return x**2 - 9   # cambia función

def derivada(x):
    return 2*x        # cambia derivada

valor = float(input("Valor inicial: "))
precision = float(input("Tolerancia: "))

while True:

    siguiente = valor - formula(valor) / derivada(valor)

    if abs(siguiente - valor) < precision:
        break

    valor = siguiente

print("Raíz encontrada:", siguiente)
```

## Observaciones

- Debe modificarse la función y su derivada
- Requiere un valor inicial cercano a la raíz
- Tiene convergencia muy rápida

---

# Conclusión

Los métodos numéricos permiten aproximar soluciones de ecuaciones cuando no es posible resolverlas algebraicamente.

Cada método tiene características diferentes en velocidad, precisión y facilidad de implementación.