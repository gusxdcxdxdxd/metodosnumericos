def formula(valor):
    return valor**2 - 2*valor + 3

x0 = 0
x1 = 2

area_aprox = ((x1 - x0) / 2) * (
    formula(x0) + formula(x1)
)

print(area_aprox)