def funcion(x, y):
    return y - x

x = 0
y = 2

incremento = 0.1

for paso in range(5):
    y = y + incremento * funcion(x, y)
    x = x + incremento

print(y)