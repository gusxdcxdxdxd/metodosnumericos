def ecuacion(x, y):
    return x**2 + y

def segunda_derivada(x, y):
    return x**2 + y + 2*x

x = 0
y = 1
h = 0.2

for ciclo in range(5):

    y = (
        y
        + h * ecuacion(x, y)
        + ((h**2) / 2) * segunda_derivada(x, y)
    )

    x = x + h

print(y)