# Tema 1: Errores

# Subtema: Problemas de precisión en comparaciones

---

# Descripción

En algunos casos, los números decimales y las raíces cuadradas no se almacenan exactamente dentro de la computadora.

Esto provoca que comparaciones aparentemente correctas den como resultado `False`, aunque matemáticamente deberían ser verdaderas.

---

# Ejemplo 1

## Código

```python
from math import sqrt

numero = sqrt(5)

respuesta = numero * numero

print(respuesta == 5)
```

## Resultado

```text
False
```

## Explicación

La raíz cuadrada de 5 contiene muchos decimales infinitos.  
Python utiliza una aproximación y por eso la comparación exacta falla.

---

# Ejemplo 2

## Código

```python
decimal1 = 0.4
decimal2 = 0.2

print(decimal1 + decimal2 == 0.6)
```

## Resultado

```text
False
```

## Explicación

Los números decimales no siempre pueden representarse exactamente en binario, causando pequeños errores internos.

---

# Ejemplo 3

## Código

```python
import math

valor = math.sqrt(7)

resultado_final = valor ** 2

print(resultado_final == 7)
```

## Resultado

```text
False
```

## Explicación

Aunque elevar al cuadrado debería devolver el mismo número, la precisión limitada genera una pequeña diferencia.

---

# Ejemplo 4

## Código

```python
cantidad = 0.9
resta = 0.4

comparacion = cantidad - resta

print(comparacion == 0.5)
```

## Resultado

```text
False
```

## Explicación

Las operaciones con números decimales producen aproximaciones mínimas que afectan las comparaciones directas.

---

# Ejemplo 5

## Código

```python
a = 0.8
b = 0.1

resultado = a + b

print(resultado == 0.9)
```

## Resultado

```text
False
```

## Explicación

Aunque el resultado parece correcto visualmente, internamente existe una pequeña diferencia decimal.

---

# Conclusión

Las computadoras manejan aproximaciones numéricas y no valores exactos en muchos casos.

Por ello, comparar números decimales usando `==` puede generar resultados inesperados.