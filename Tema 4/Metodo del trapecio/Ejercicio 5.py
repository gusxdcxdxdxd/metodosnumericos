def funcion_principal(x):
    return x**3 - x

a = 1
b = 3

resultado_final = ((b - a) / 2) * (
    funcion_principal(a)
    + funcion_principal(b)
)

print(resultado_final)