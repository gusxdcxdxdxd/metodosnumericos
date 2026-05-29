def funcion_principal(x):
    return x**3 - 2*x

inicio = 1
fin = 4

medio = (inicio + fin) / 2

resultado_final = ((fin - inicio) / 6) * (
    funcion_principal(inicio)
    + 4 * funcion_principal(medio)
    + funcion_principal(fin)
)

print(resultado_final)