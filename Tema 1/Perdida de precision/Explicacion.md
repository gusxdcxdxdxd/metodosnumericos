# Tema 1: Errores

# Subtema: Pérdida de precisión por diferencia de magnitud

---

# Descripción

Este tipo de error ocurre cuando se realizan operaciones entre números extremadamente grandes y números muy pequeños.

Debido a la precisión limitada de los números flotantes, el valor pequeño puede desaparecer completamente en el resultado final.

---

# Ejemplo 1

## Código

```python
numero_mayor = 8e15

print(numero_mayor + 7)
```

## Resultado

```text
8000000000000000.0
```

## Explicación

El valor 7 es demasiado pequeño comparado con `8e15`, por lo que se pierde durante la operación.

---

# Ejemplo 2

## Código

```python
cantidad = 4e16

resultado = cantidad + 9

print(resultado)
```

## Resultado

```text
4e+16
```

## Explicación

La computadora mantiene únicamente la parte más significativa del número y descarta el valor pequeño.

---

# Ejemplo 3

## Código

```python
valor_grande = 6e14

print(valor_grande + 1)
```

## Resultado

```text
600000000000000.0
```

## Explicación

Aunque se suma 1, la magnitud del número grande impide que el cambio sea visible.

---

# Ejemplo 4

## Código

```python
dato = 2e17

operacion = dato + 15

print(operacion)
```

## Resultado

```text
2e+17
```

## Explicación

El número pequeño no afecta el resultado debido a las limitaciones de precisión flotante.

---

# Ejemplo 5

## Código

```python
numero = 3e16

print(numero + 8)
```

## Resultado

```text
30000000000000000.0
```

## Explicación

La diferencia de magnitudes provoca que el valor pequeño desaparezca en la representación interna.

---

# Conclusión

Cuando un número muy pequeño se combina con uno extremadamente grande, el valor pequeño puede perderse completamente.

Esto ocurre por la precisión limitada que tienen los números flotantes en la computadora.