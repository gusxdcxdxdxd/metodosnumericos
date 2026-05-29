# Tema 1: Errores

## Subtema: Acumulación de errores

## Descripción

La acumulación de errores ocurre cuando una operación se repite muchas veces y pequeños errores de redondeo se van sumando.

---

# Código 1

## Código

```python
total = 0

for x in range(7000):
    total += 0.07

print(total)
```

## Resultado

```text
489.999999999...
```

## Explicación

Se suma 0.07 muchas veces y aparecen pequeñas diferencias por el manejo decimal de Python.

---

# Código 2

## Código

```python
resultado = 0

for n in range(9000):
    resultado += 0.11

print(resultado)
```

## Resultado

```text
989.99999999...
```

## Explicación

Los errores de redondeo aumentan conforme se repite la suma.

---

# Código 3

## Código

```python
acumulado = 0

for dato in range(4000):
    acumulado += 0.25

print(acumulado)
```

## Resultado

```text
1000.0
```

## Explicación

Algunos números se representan mejor en binario y generan menos error.

---

# Código 4

## Código

```python
valor = 0

for numero in range(6000):
    valor += 0.13

print(valor)
```

## Resultado

```text
779.99999999...
```

## Explicación

Los pequeños errores se acumulan después de miles de operaciones.

---

# Código 5

## Código

```python
contador = 0

for elemento in range(8000):
    contador += 0.06

print(contador)
```

## Resultado

```text
479.99999999...
```

## Explicación

La representación decimal interna provoca diferencias mínimas en el resultado.

---

# Conclusión

Los errores de acumulación aparecen cuando una computadora trabaja con números decimales repetidamente.