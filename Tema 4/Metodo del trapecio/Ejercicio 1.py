def funcion(valor):
    return valor**2 + 1

inicio = 0
fin = 3

area = ((fin - inicio) / 2) * (
    funcion(inicio) + funcion(fin)
)

print(area)