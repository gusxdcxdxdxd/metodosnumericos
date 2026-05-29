def evaluar(x):

    x0 = 0
    y0 = 0

    x1 = 2
    y1 = 4

    x2 = 4
    y2 = 16

    a = y0 * ((x - x1)*(x - x2)) / ((x0 - x1)*(x0 - x2))
    b = y1 * ((x - x0)*(x - x2)) / ((x1 - x0)*(x1 - x2))
    c = y2 * ((x - x0)*(x - x1)) / ((x2 - x0)*(x2 - x1))

    return a + b + c

print(evaluar(3))