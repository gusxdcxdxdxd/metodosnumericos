def interpolar(valor):

    a = 0
    b = 1

    c = 2
    d = 5

    e = 4
    f = 17

    termino1 = b * ((valor - c)*(valor - e)) / ((a - c)*(a - e))
    termino2 = d * ((valor - a)*(valor - e)) / ((c - a)*(c - e))
    termino3 = f * ((valor - a)*(valor - c)) / ((e - a)*(e - c))

    return termino1 + termino2 + termino3

print(interpolar(3))