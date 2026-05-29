def formula(dato):
    return dato**3 - dato - 6

valor1 = 1
valor2 = 3

for ciclo in range(10):

    solucion = valor2 - (
        formula(valor2) * (valor1 - valor2)
    ) / (formula(valor1) - formula(valor2))

    if formula(valor1) * formula(solucion) < 0:
        valor2 = solucion
    else:
        valor1 = solucion

print(solucion)