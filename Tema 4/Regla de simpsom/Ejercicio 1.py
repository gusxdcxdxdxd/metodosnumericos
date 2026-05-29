def funcion(valor):
    return valor**2 + 2

inicio = 0
fin = 2

medio = (inicio + fin) / 2

integral = ((fin - inicio) / 6) * (
    funcion(inicio)
    + 4 * funcion(medio)
    + funcion(fin)
)

print(integral)