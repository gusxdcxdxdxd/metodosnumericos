def aproximar(x):

    xa = 2
    ya = 4

    xb = 4
    yb = 12

    xc = 6
    yc = 28

    t1 = ya * ((x - xb)*(x - xc)) / ((xa - xb)*(xa - xc))
    t2 = yb * ((x - xa)*(x - xc)) / ((xb - xa)*(xb - xc))
    t3 = yc * ((x - xa)*(x - xb)) / ((xc - xa)*(xc - xb))

    return t1 + t2 + t3

print(aproximar(5))