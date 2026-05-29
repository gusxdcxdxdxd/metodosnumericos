def funcion(x):
    return x**2 + 2

inicio = 0
fin = 3

paso = (fin - inicio) / 3

punto0 = inicio
punto1 = inicio + paso
punto2 = inicio + 2 * paso
punto3 = fin

resultado = (3 * paso / 8) * (
    funcion(punto0)
    + 3 * funcion(punto1)
    + 3 * funcion(punto2)
    + funcion(punto3)
)

print(resultado)