def derivada(x, y):
    return 2*x + y

x_actual = 0
y_actual = 1

paso = 0.1

for iteracion in range(5):
    y_actual = y_actual + paso * derivada(x_actual, y_actual)
    x_actual = x_actual + paso

print(y_actual)