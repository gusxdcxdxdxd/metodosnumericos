def modelo(x, y):
    return x**2 + y

x = 0
y = 1
h = 0.2

for ciclo in range(5):

    k1 = h * modelo(x, y)
    k2 = h * modelo(x + h/2, y + k1/2)
    k3 = h * modelo(x + h/2, y + k2/2)
    k4 = h * modelo(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x += h

print(y)