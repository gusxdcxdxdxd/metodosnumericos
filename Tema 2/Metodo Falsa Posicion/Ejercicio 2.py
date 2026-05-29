def funcion(numero):
    return numero**2 - 16

inicio = 2
fin = 5

for i in range(8):

    medio = fin - (
        funcion(fin) * (inicio - fin)
    ) / (funcion(inicio) - funcion(fin))

    if funcion(inicio) * funcion(medio) < 0:
        fin = medio
    else:
        inicio = medio

print(medio)