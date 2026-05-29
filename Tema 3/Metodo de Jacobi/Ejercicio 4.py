x = y = z = 0

for intento in range(20):

    nx = (18 - y - z) / 10
    ny = (25 - 2*x - z) / 11
    nz = (27 - x - 2*y) / 10

    x = nx
    y = ny
    z = nz

print(x, y, z)