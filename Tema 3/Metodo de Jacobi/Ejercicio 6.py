x = y = z = w = v = 0

for repeticion in range(30):

    nx = (24 - y - z - w - v) / 12
    ny = (28 - x - z - w - v) / 11
    nz = (30 - x - y - w - v) / 10
    nw = (35 - x - y - z - v) / 9
    nv = (40 - x - y - z - w) / 8

    x = nx
    y = ny
    z = nz
    w = nw
    v = nv

print(x, y, z, w, v)