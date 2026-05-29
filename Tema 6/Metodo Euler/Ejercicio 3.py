def ecuacion(x, y):
    return x**2 + y

x = 0
y = 1

h = 0.2

for i in range(5):
    y = y + h * ecuacion(x, y)
    x = x + h

print(y)