def operacion(x):
    return x**3 - 5*x + 2

a = 0
b = 1

for intento in range(9):

    aproximacion = b - (
        operacion(b) * (a - b)
    ) / (operacion(a) - operacion(b))

    if operacion(a) * operacion(aproximacion) < 0:
        b = aproximacion
    else:
        a = aproximacion

print(aproximacion)