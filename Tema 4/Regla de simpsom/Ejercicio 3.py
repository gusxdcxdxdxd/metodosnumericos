def expresion(numero):
    return numero**3 + 1

limite_inferior = 1
limite_superior = 3

punto_medio = (limite_inferior + limite_superior) / 2

area = ((limite_superior - limite_inferior) / 6) * (
    expresion(limite_inferior)
    + 4 * expresion(punto_medio)
    + expresion(limite_superior)
)

print(area)