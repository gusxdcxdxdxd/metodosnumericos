def operacion(x):
    return x**3 - 6*x + 1

def derivada_operacion(x):
    return 3*x**2 - 6

resultado = 2

for intento in range(10):
    resultado = resultado - operacion(resultado) / derivada_operacion(resultado)

print(resultado)