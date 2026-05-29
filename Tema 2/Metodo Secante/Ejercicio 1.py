def ecuacion(valor):
    return valor**3 - 2*valor - 3

inicio = 1
final = 3

for paso in range(10):

    mitad = (inicio + final) / 2

    if ecuacion(inicio) * ecuacion(mitad) < 0:
        final = mitad
    else:
        inicio = mitad
