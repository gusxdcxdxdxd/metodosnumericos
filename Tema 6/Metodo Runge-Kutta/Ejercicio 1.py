def derivada(x, y):
    return 2*x + y

x = 0
y = 1
h = 0.1

for paso in range(5):

    k1 = h * derivada(x, y)
    k2 = h * derivada(x + h/2, y + k1/2)
    k3 = h * derivada(x + h/2, y + k2/2)
    k4 = h * derivada(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h

print(y)