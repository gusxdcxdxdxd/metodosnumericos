def funcion(x, y):
    return 3*x - y

def segunda(x, y):
    return 3 - (3*x - y)

x = 0
y = 1
h = 0.1

for contador in range(5):

    y = (
        y
        + h * funcion(x, y)
        + ((h**2) / 2) * segunda(x, y)
    )

    x = x + h

print(y)