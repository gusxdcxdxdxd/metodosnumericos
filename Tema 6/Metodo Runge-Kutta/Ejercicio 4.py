def pendiente(x, y):
    return x + 2*y

x_actual = 0
y_actual = 1
paso = 0.1

for vuelta in range(5):

    p1 = paso * pendiente(x_actual, y_actual)
    p2 = paso * pendiente(x_actual + paso/2, y_actual + p1/2)
    p3 = paso * pendiente(x_actual + paso/2, y_actual + p2/2)
    p4 = paso * pendiente(x_actual + paso, y_actual + p3)

    y_actual = y_actual + (p1 + 2*p2 + 2*p3 + p4) / 6
    x_actual = x_actual + paso

print(y_actual)