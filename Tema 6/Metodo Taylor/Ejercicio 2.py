def f(x, y):
    return y - x

def derivada2(x, y):
    return y - x - 1

x = 0
y = 2
h = 0.1

for i in range(5):

    y = (
        y
        + h * f(x, y)
        + ((h**2) / 2) * derivada2(x, y)
    )

    x += h

print(y)