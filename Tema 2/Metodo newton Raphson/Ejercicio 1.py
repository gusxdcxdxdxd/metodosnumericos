def funcion(valor):
    return valor**3 - 2*valor - 1

def derivada(valor):
    return 3*valor**2 - 2

aproximacion = 1.5

for paso in range(8):
    aproximacion = aproximacion - funcion(aproximacion) / derivada(aproximacion)

print(aproximacion)