def ecuacion(valor):
    return 4 * valor + 1

a = 1
b = 4

h = (b - a) / 3

x0 = a
x1 = a + h
x2 = a + 2 * h
x3 = b

area = (3 * h / 8) * (
    ecuacion(x0)
    + 3 * ecuacion(x1)
    + 3 * ecuacion(x2)
    + ecuacion(x3)
)

print(area)