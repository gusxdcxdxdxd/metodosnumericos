x_actual = 0
y_actual = 0

for paso in range(12):
    x_actual = (17 + y_actual) / 6
    y_actual = (31 - 2*x_actual) / 5

print(x_actual, y_actual)