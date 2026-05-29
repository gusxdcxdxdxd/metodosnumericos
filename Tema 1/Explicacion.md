# Tema: Tipos de Error en Métodos Numéricos

---

# Introducción

En los métodos numéricos es importante conocer qué tan cerca se encuentra un resultado aproximado del valor verdadero.

Para medir esa diferencia se utilizan distintos tipos de error matemático, los cuales ayudan a determinar la precisión de los cálculos realizados.

---

# Error absoluto

El error absoluto muestra la diferencia directa entre el valor exacto y el valor aproximado.

Este error únicamente indica cuánto cambia un resultado respecto al valor real.

## Fórmula

```text
Ea = |valor exacto - valor aproximado|
```

---

# Error relativo

El error relativo compara el tamaño del error absoluto con respecto al valor real.

Sirve para analizar qué tan importante es el error dependiendo de la magnitud del número.

## Fórmula

```text
Er = Ea / valor exacto
```

---

# Error porcentual

El error porcentual representa el error relativo expresado en porcentaje.

Es una de las formas más utilizadas porque facilita interpretar el nivel de precisión.

## Fórmula

```text
E% = Er × 100
```

---

# Programa

## Código

```python
real = float(input("Escribe el valor exacto: "))
aproximado = float(input("Escribe el valor calculado: "))

absoluto = abs(real - aproximado)

relativo = absoluto / real

porcentaje = relativo * 100

print("\nRESULTADOS")
print("Error absoluto =", absoluto)
print("Error relativo =", relativo)
print("Error porcentual =", porcentaje, "%")
```

---

# Explicación del programa

El programa solicita dos valores:

- El valor exacto
- El valor aproximado

Después calcula automáticamente:

- El error absoluto
- El error relativo
- El error porcentual

Finalmente muestra los resultados obtenidos en pantalla.

---

# Ejemplo de ejecución

```text
Escribe el valor exacto: 50
Escribe el valor calculado: 47
```

## Resultado

```text
RESULTADOS
Error absoluto = 3
Error relativo = 0.06
Error porcentual = 6.0 %
```

---

# Conclusión

Los tipos de error permiten evaluar la precisión de un método numérico.

Gracias a ellos es posible saber qué tan confiable es un resultado aproximado comparándolo con el valor real.