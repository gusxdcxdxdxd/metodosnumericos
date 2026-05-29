def ecuacion(x):
    return 3*x + 2

a = 1
b = 5

centro = (a + b) / 2

resultado = ((b - a) / 6) * (
    ecuacion(a)
    + 4 * ecuacion(centro)
    + ecuacion(b)
)

print(resultado)