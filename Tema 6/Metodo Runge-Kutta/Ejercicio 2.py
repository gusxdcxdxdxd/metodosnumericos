def funcion(x, y):
    return y - x

valor_x = 0
valor_y = 2
delta = 0.1

for i in range(5):

    a = delta * funcion(valor_x, valor_y)
    b = delta * funcion(valor_x + delta/2, valor_y + a/2)
    c = delta * funcion(valor_x + delta/2, valor_y + b/2)
    d = delta * funcion(valor_x + delta, valor_y + c)

    valor_y = valor_y + (a + 2*b + 2*c + d) / 6
    valor_x = valor_x + delta

print(valor_y)