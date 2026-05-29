def calcular(x):

    x1 = 1
    y1 = 3

    x2 = 2
    y2 = 8

    x3 = 4
    y3 = 24

    p1 = y1 * ((x - x2)*(x - x3)) / ((x1 - x2)*(x1 - x3))
    p2 = y2 * ((x - x1)*(x - x3)) / ((x2 - x1)*(x2 - x3))
    p3 = y3 * ((x - x1)*(x - x2)) / ((x3 - x1)*(x3 - x2))

    return p1 + p2 + p3

print(calcular(3))