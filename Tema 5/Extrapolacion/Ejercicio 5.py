x0 = 2
y0 = 7

x1 = 6
y1 = 19

x = 9

valor_estimado = y0 + (
    (y1 - y0) /
    (x1 - x0)
) * (x - x0)

print(valor_estimado)
