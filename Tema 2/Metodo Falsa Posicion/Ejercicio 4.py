def expresion(valor):
    return valor**2 - 7

limite1 = 2
limite2 = 3

for vuelta in range(10):

    raiz = limite2 - (
        expresion(limite2) * (limite1 - limite2)
    ) / (expresion(limite1) - expresion(limite2))

    if expresion(limite1) * expresion(raiz) < 0:
        limite2 = raiz
    else:
        limite1 = raiz

print(raiz)