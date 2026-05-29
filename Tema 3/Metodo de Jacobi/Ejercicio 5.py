x = y = z = w = 0

for ciclo in range(25):

    nx = (22 - y - z - w) / 8
    ny = (20 - x - z - w) / 7
    nz = (18 - x - y - w) / 6
    nw = (24 - x - y - z) / 5

    x = nx
    y = ny
    z = nz
    w = nw

print(x, y, z, w)