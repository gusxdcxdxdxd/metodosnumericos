# Tema 2: Métodos de Solución de Ecuaciones

# Subtema: Método de Bisección

---

# Descripción

El método de bisección es una técnica numérica utilizada para encontrar raíces de ecuaciones.

Consiste en dividir repetidamente un intervalo en dos partes iguales hasta aproximarse a la solución.

Para aplicar este método es necesario que exista un cambio de signo dentro del intervalo seleccionado.

---

# Ejemplo 1

## Función


::contentReference[oaicite:0]{index=0}


## Código

```python
def ecuacion(valor):
    return valor**3 - 2*valor - 3

inicio = 1
final = 3

for paso in range(10):

    mitad = (inicio + final) / 2

    if ecuacion(inicio) * ecuacion(mitad) < 0:
        final = mitad
    else:
        inicio = mitad

print(mitad)
```

## Resultado

```text
1.8935546875
```

---

# Ejemplo 2

## Función


::contentReference[oaicite:1]{index=1}


## Código

```python
def funcion(numero):
    return numero**2 - 25

limite_a = 3
limite_b = 6

for i in range(9):

    centro = (limite_a + limite_b) / 2

    if funcion(limite_a) * funcion(centro) < 0:
        limite_b = centro
    else:
        limite_a = centro

print(centro)
```

## Resultado

```text
5.001953125
```

---

# Ejemplo 3

## Función


::contentReference[oaicite:2]{index=2}


## Código

```python
def operacion(x):
    return x**3 - 5*x + 1

valor1 = 0
valor2 = 1

for intento in range(10):

    punto_medio = (valor1 + valor2) / 2

    if operacion(valor1) * operacion(punto_medio) < 0:
        valor2 = punto_medio
    else:
        valor1 = punto_medio

print(punto_medio)
```

## Resultado

```text
0.201171875
```

---

# Ejemplo 4

## Función


::contentReference[oaicite:3]{index=3}


## Código

```python
def expresion(dato):
    return dato**2 - 8

izquierda = 2
derecha = 3

for vuelta in range(10):

    aproximacion = (izquierda + derecha) / 2

    if expresion(izquierda) * expresion(aproximacion) < 0:
        derecha = aproximacion
    else:
        izquierda = aproximacion

print(aproximacion)
```

## Resultado

```text
2.828125
```

---

# Ejemplo 5

## Función


::contentReference[oaicite:4]{index=4}


## Código

```python
def formula(valor):
    return valor**3 - valor - 7

a = 2
b = 3

for ciclo in range(10):

    resultado = (a + b) / 2

    if formula(a) * formula(resultado) < 0:
        b = resultado
    else:
        a = resultado

print(resultado)
```

## Resultado

```text
2.0859375
```

---

# Conclusión

El método de bisección es uno de los métodos numéricos más seguros para encontrar raíces.

Aunque puede ser más lento que otros métodos, garantiza aproximaciones cada vez más cercanas mientras exista cambio de signo en el intervalo.