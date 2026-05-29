x = 0
y = 0

for paso in range(12):

    nuevo_x = (11 - y) / 4
    nuevo_y = (9 - x) / 3

    x = nuevo_x
    y = nuevo_y

print(x, y)