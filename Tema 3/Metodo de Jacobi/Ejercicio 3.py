valor_x = 0
valor_y = 0

for i in range(15):

    nuevo_x = (17 + valor_y) / 6
    nuevo_y = (31 - 2*valor_x) / 5

    valor_x = nuevo_x
    valor_y = nuevo_y

print(valor_x, valor_y)