def pendiente(x, y):
    return x + 2*y

valor_x = 0
valor_y = 1

delta = 0.1

for vuelta in range(5):
    valor_y = valor_y + delta * pendiente(valor_x, valor_y)
    valor_x = valor_x + delta

print(valor_y)