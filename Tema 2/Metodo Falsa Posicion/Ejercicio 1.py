def ecuacion(valor):
    return valor**3 - 3*valor - 1

izquierda = 1
derecha = 2

for paso in range(10):

    punto = derecha - (
        ecuacion(derecha) * (izquierda - derecha)
    ) / (ecuacion(izquierda) - ecuacion(derecha))

    if ecuacion(izquierda) * ecuacion(punto) < 0:
        derecha = punto
    else:
        izquierda = punto

print(punto)