def formula(valor):
    return valor**2 - 3*valor + 4

x0 = 0
x1 = 3

xm = (x0 + x1) / 2

aproximacion = ((x1 - x0) / 6) * (
    formula(x0)
    + 4 * formula(xm)
    + formula(x1)
)

print(aproximacion)