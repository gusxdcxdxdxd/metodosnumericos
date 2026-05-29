x0 = 0
y0 = 2

x1 = 8
y1 = 18

punto = 5

valor_interpolado = y0 + (
    (y1 - y0)
    / (x1 - x0)
) * (punto - x0)

print(valor_interpolado)