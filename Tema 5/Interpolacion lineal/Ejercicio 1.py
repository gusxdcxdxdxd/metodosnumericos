x_inicial = 2
y_inicial = 4

x_final = 6
y_final = 12

valor = 4

resultado = y_inicial + (
    (y_final - y_inicial)
    / (x_final - x_inicial)
) * (valor - x_inicial)

print(resultado)