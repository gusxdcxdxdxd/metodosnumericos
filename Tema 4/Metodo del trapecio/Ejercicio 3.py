def expresion(x):
    return x**3 + 2

limite_inferior = 1
limite_superior = 4

integral = ((limite_superior - limite_inferior) / 2) * (
    expresion(limite_inferior)
    + expresion(limite_superior)
)

print(integral)