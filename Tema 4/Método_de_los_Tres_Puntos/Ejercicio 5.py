def funcion_principal(x):
    return x**3 - x

punto = 1.5
incremento = 0.1

valor_derivada = (
    funcion_principal(punto + incremento)
    - funcion_principal(punto - incremento)
) / (2 * incremento)

print(valor_derivada)