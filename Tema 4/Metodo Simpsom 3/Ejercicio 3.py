def expresion(numero):
    return numero**3 + 3

limite_inferior = 1
limite_superior = 4

incremento = (limite_superior - limite_inferior) / 3

x0 = limite_inferior
x1 = limite_inferior + incremento
x2 = limite_inferior + 2 * incremento
x3 = limite_superior

integral = (3 * incremento / 8) * (
    expresion(x0)
    + 3 * expresion(x1)
    + 3 * expresion(x2)
    + expresion(x3)
)

print(integral)