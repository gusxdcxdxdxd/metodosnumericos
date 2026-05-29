x_inicial = 2
y_inicial = 4

x_final = 5
y_final = 10

valor_buscado = 7

estimacion = y_inicial + (
    (y_final - y_inicial) /
    (x_final - x_inicial)
) * (valor_buscado - x_inicial)

print(estimacion)
