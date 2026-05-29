def ecuacion(numero):
    return 3 * numero + 2

a = 1
b = 5

resultado = ((b - a) / 2) * (
    ecuacion(a) + ecuacion(b)
)

print(resultado)