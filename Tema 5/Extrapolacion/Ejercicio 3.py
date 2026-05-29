dato_x1 = 0
dato_y1 = 2

dato_x2 = 4
dato_y2 = 14

nuevo_x = 6

nuevo_y = dato_y1 + (
    (dato_y2 - dato_y1) /
    (dato_x2 - dato_x1)
) * (nuevo_x - dato_x1)

print(nuevo_y)