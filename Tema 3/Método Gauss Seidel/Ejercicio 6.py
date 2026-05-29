x = y = z = w = v = 0

for repeticion in range(30):
    x = (20 - y - z - w - v) / 12
    y = (25 - x - z - w - v) / 11
    z = (30 - x - y - w - v) / 10
    w = (35 - x - y - z - v) / 9
    v = (40 - x - y - z - w) / 8

print(x, y, z, w, v)