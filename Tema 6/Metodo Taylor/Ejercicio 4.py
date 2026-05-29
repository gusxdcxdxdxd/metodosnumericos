def pendiente(x, y):
    return x + 2*y

def auxiliar(x, y):
    return 1 + 2*x + 4*y

x = 0
y = 1
h = 0.1

for vuelta in range(5):

    y = (
        y
        + h * pendiente(x, y)
        + (h**2 / 2) * auxiliar(x, y)
    )

    x = x + h

print(y)