# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

---

# Descripción General

Los sistemas de ecuaciones lineales aparecen cuando se necesita encontrar varios valores desconocidos que cumplen distintas ecuaciones al mismo tiempo.

Para resolverlos existen métodos directos e iterativos.  
Los métodos directos buscan obtener la solución en un número definido de pasos, mientras que los iterativos aproximan la respuesta poco a poco.

---

# Eliminación Gaussiana

La eliminación gaussiana convierte la matriz del sistema en una matriz triangular superior.  
Después se aplica sustitución hacia atrás para obtener las incógnitas.

## Código

```python
import numpy as np

cantidad = int(input("Cantidad de ecuaciones: "))

coeficientes = []
resultados = []

print("Escribe los coeficientes de cada fila:")

for fila in range(cantidad):
    datos = list(map(float, input(f"Ecuación {fila + 1}: ").split()))
    coeficientes.append(datos)

print("Escribe los términos independientes:")

for fila in range(cantidad):
    dato = float(input(f"Resultado {fila + 1}: "))
    resultados.append(dato)

A = np.array(coeficientes, dtype=float)
B = np.array(resultados, dtype=float)

for i in range(cantidad):
    for j in range(i + 1, cantidad):
        multiplicador = A[j][i] / A[i][i]
        A[j] = A[j] - multiplicador * A[i]
        B[j] = B[j] - multiplicador * B[i]

solucion = np.zeros(cantidad)

for i in range(cantidad - 1, -1, -1):
    solucion[i] = (B[i] - np.dot(A[i][i+1:], solucion[i+1:])) / A[i][i]

print("Valores encontrados:")
print(solucion)
```

## Ejemplo de entrada

```text
Ecuación 1: 3 2 -1
Ecuación 2: 2 -2 4
Ecuación 3: -1 0.5 -1
Resultado 1: 1
Resultado 2: -2
Resultado 3: 0
```

---

# Método de Gauss-Jordan

Gauss-Jordan trabaja con una matriz aumentada y la transforma hasta que la parte de coeficientes se convierte en matriz identidad.

Al final, la última columna contiene directamente la solución.

## Código

```python
import numpy as np

orden = int(input("Número de ecuaciones: "))

matriz = []

print("Ingresa la matriz aumentada:")

for fila in range(orden):
    valores = list(map(float, input(f"Fila {fila + 1}: ").split()))
    matriz.append(valores)

matriz = np.array(matriz, dtype=float)

for i in range(orden):

    matriz[i] = matriz[i] / matriz[i][i]

    for j in range(orden):

        if i != j:
            factor = matriz[j][i]
            matriz[j] = matriz[j] - factor * matriz[i]

print("Matriz final reducida:")
print(matriz)
```

## Ejemplo de entrada

```text
Fila 1: 3 2 -1 1
Fila 2: 2 -2 4 -2
Fila 3: -1 0.5 -1 0
```

---

# Método de Gauss-Seidel

Gauss-Seidel es un método iterativo.  
Su característica principal es que utiliza los valores más recientes en cuanto se calculan.

## Código

```python
variables = int(input("Número de variables: "))

A = []
B = []

print("Ingresa los coeficientes:")

for i in range(variables):
    fila = list(map(float, input(f"Fila {i + 1}: ").split()))
    A.append(fila)

print("Ingresa el vector de resultados:")

for i in range(variables):
    valor = float(input(f"Resultado {i + 1}: "))
    B.append(valor)

vueltas = int(input("Número de iteraciones: "))

x = [0 for i in range(variables)]

for k in range(vueltas):

    for i in range(variables):

        suma = 0

        for j in range(variables):

            if i != j:
                suma += A[i][j] * x[j]

        x[i] = (B[i] - suma) / A[i][i]

print("Aproximación obtenida:")
print(x)
```

## Ejemplo de entrada

```text
Fila 1: 6 1 1
Fila 2: 2 7 1
Fila 3: 1 1 5
Resultado 1: 8
Resultado 2: 10
Resultado 3: 7
```

---

# Método de Jacobi

El método de Jacobi también es iterativo, pero a diferencia de Gauss-Seidel, no usa los valores nuevos de inmediato.

Cada nueva aproximación se calcula con los valores de la iteración anterior.

## Código

```python
n = int(input("Cantidad de variables: "))

matriz = []
vector = []

print("Escribe la matriz de coeficientes:")

for i in range(n):
    fila = list(map(float, input(f"Fila {i + 1}: ").split()))
    matriz.append(fila)

print("Escribe los términos independientes:")

for i in range(n):
    valor = float(input(f"Término {i + 1}: "))
    vector.append(valor)

iteraciones = int(input("Iteraciones a realizar: "))

actual = [0 for i in range(n)]

for k in range(iteraciones):

    nuevo = actual.copy()

    for i in range(n):

        suma = 0

        for j in range(n):

            if i != j:
                suma += matriz[i][j] * actual[j]

        nuevo[i] = (vector[i] - suma) / matriz[i][i]

    actual = nuevo

print("Solución aproximada:")
print(actual)
```

## Ejemplo de entrada

```text
Fila 1: 6 1 1
Fila 2: 2 7 1
Fila 3: 1 1 5
Término 1: 8
Término 2: 10
Término 3: 7
```

---

# Conclusión

Los métodos para resolver sistemas de ecuaciones permiten encontrar valores desconocidos que satisfacen varias ecuaciones al mismo tiempo.

Gauss y Gauss-Jordan son métodos directos, mientras que Jacobi y Gauss-Seidel son métodos iterativos que aproximan la solución mediante repeticiones.