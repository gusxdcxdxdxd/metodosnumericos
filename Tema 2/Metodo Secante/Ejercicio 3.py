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