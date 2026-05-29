x = y = z = w = 0

for intento in range(25):
    x = (18 - y - z - w) / 8
    y = (20 - x - z - w) / 7
    z = (22 - x - y - w) / 6
    w = (24 - x - y - z) / 5

print(x, y, z, w)