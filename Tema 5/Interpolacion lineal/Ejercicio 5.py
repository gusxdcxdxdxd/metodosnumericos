dato_x1 = 2
dato_y1 = 6

dato_x2 = 7
dato_y2 = 21

valor_x = 4

valor_y = dato_y1 + (
    (dato_y2 - dato_y1)
    / (dato_x2 - dato_x1)
) * (valor_x - dato_x1)

print(valor_y)