def funcion(numero):
    return numero**2 - 25

limite_a = 3
limite_b = 6

for i in range(9):

    centro = (limite_a + limite_b) / 2

    if funcion(limite_a) * funcion(centro) < 0:
        limite_b = centro
    else:
        limite_a = centro

print(centro)