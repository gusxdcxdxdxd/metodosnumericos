def primera(x, y):
    return 2*x + y

def segunda(x, y):
    return 2 + 2*x + y

x = 0
y = 1
h = 0.1

for paso in range(5):

    y = (
        y
        + h * primera(x, y)
        + (h**2 / 2) * segunda(x, y)
    )

    x = x + h

print(y)