def funcion(valor):
    return valor**2 + 3*valor

punto = 2
incremento = 0.1

derivada = (
    funcion(punto + incremento)
    - funcion(punto - incremento)
) / (2 * incremento)

print(derivada)