def modelo(x, y):
    return 3*x - y

x = 0
y = 1

h = 0.1

for contador in range(5):
    y = y + h * modelo(x, y)
    x = x + h

print(y)