def expresion(valor):
    return valor**3 - valor - 4

def derivada_expresion(valor):
    return 3*valor**2 - 1

raiz = 2

for ciclo in range(9):
    raiz = raiz - expresion(raiz) / derivada_expresion(raiz)

print(raiz)