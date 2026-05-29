def expresion(x):
    return x**3 + 2*x

valor = 2
h = 0.1

aproximacion = (
    expresion(valor + h)
    - expresion(valor - h)
) / (2 * h)

print(aproximacion)