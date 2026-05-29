# Tema 2: Métodos de Solución de Ecuaciones

# Subtema: Método de Newton-Raphson

---

# Descripción

El método de Newton-Raphson es un procedimiento numérico utilizado para encontrar raíces de ecuaciones.

Este método utiliza derivadas para generar aproximaciones cada vez más cercanas a la solución real.

Se caracteriza por tener una convergencia rápida cuando el valor inicial es adecuado.

---

# Ejemplo 1

## Función


::contentReference[oaicite:0]{index=0}


## Derivada

:contentReference[oaicite:1]{index=1}

## Código

```python
def funcion(valor):
    return valor**3 - 2*valor - 1

def derivada(valor):
    return 3*valor**2 - 2

aproximacion = 1.5

for paso in range(8):
    aproximacion = aproximacion - funcion(aproximacion) / derivada(aproximacion)

print(aproximacion)
```

## Resultado

```text
1.618033988749895
```

---

# Ejemplo 2

## Función


::contentReference[oaicite:2]{index=2}


## Derivada

:contentReference[oaicite:3]{index=3}

## Código

```python
def ecuacion(numero):
    return numero**2 - 9

def pendiente(numero):
    return 2 * numero

valor = 4

for i in range(6):
    valor = valor - ecuacion(valor) / pendiente(valor)

print(valor)
```

## Resultado

```text
3.0
```

---

# Ejemplo 3

## Función


::contentReference[oaicite:4]{index=4}


## Derivada

:contentReference[oaicite:5]{index=5}

## Código

```python
def operacion(x):
    return x**3 - 6*x + 1

def derivada_operacion(x):
    return 3*x**2 - 6

resultado = 2

for intento in range(10):
    resultado = resultado - operacion(resultado) / derivada_operacion(resultado)

print(resultado)
```

## Resultado

```text
2.356895867892209
```

---

# Ejemplo 4

## Función


::contentReference[oaicite:6]{index=6}


## Derivada

:contentReference[oaicite:7]{index=7}

## Código

```python
def formula(dato):
    return dato**2 - 5

def cambio(dato):
    return 2 * dato

inicio = 2

for vuelta in range(7):
    inicio = inicio - formula(inicio) / cambio(inicio)

print(inicio)
```

## Resultado

```text
2.23606797749979
```

---

# Ejemplo 5

## Función


::contentReference[oaicite:8]{index=8}


## Derivada

:contentReference[oaicite:9]{index=9}

## Código

```python
def expresion(valor):
    return valor**3 - valor - 4

def derivada_expresion(valor):
    return 3*valor**2 - 1

raiz = 2

for ciclo in range(9):
    raiz = raiz - expresion(raiz) / derivada_expresion(raiz)

print(raiz)
```

## Resultado

```text
1.796321903259441
```

---

# Conclusión

El método de Newton-Raphson permite aproximar raíces de ecuaciones utilizando derivadas.

Su principal ventaja es la rapidez con la que converge hacia la solución cuando se selecciona un valor inicial adecuado.