# Tema 1: Errores

# Subtema: Desbordamiento numérico (Overflow)

---

# Descripción

El overflow ocurre cuando un número excede el límite máximo que puede almacenarse en memoria.

En algunos lenguajes esto provoca resultados incorrectos o negativos.  
Python puede manejar enteros muy grandes, pero en números flotantes sí pueden aparecer problemas de desbordamiento.

---

# Ejemplo 1

## Código

```python
numero_grande = 1500000000

resultado = numero_grande * 3

print(resultado)
```

## Resultado

```text
4500000000
```

## Explicación

Python puede trabajar con enteros grandes sin provocar overflow.

### Resultado aproximado en Java

```text
205032704
```

---

# Ejemplo 2

## Código

```python
limite = 2147483647

print(limite + 5)
```

## Resultado

```text
2147483652
```

## Explicación

En Python el entero sigue creciendo normalmente sin cambiar de signo.

### Resultado aproximado en Java

```text
-2147483644
```

---

# Ejemplo 3

## Código

```python
valor_maximo = 999999999999999999

print(valor_maximo * 10)
```

## Resultado

```text
9999999999999999990
```

## Explicación

Python utiliza precisión arbitraria en enteros, por eso puede almacenar números enormes.

### Resultado aproximado en Java

```text
Overflow numérico
```

---

# Ejemplo 4

## Código

```python
dato = 9.9e307

print(dato * 100)
```

## Resultado

```text
inf
```

## Explicación

El valor supera el límite permitido para números flotantes y Python devuelve infinito.

---

# Ejemplo 5

## Código

```python
cantidad = 5e308

print(cantidad * cantidad)
```

## Resultado

```text
inf
```

## Explicación

Los números de punto flotante tienen un límite máximo.  
Cuando se supera, aparece el valor `inf`.

---

# Conclusión

Python maneja correctamente enteros muy grandes, evitando overflow en la mayoría de los casos.

Sin embargo, los números flotantes sí tienen límites y pueden producir infinito cuando el valor es demasiado grande.