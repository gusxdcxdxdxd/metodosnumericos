x = 0
y = 0
z = 0

for ciclo in range(20):
    x = (17 - y - z) / 10
    y = (28 - 2*x - z) / 10
    z = (35 - 2*x - 3*y) / 10

print(x, y, z)