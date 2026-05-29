def expresion(dato):
    return dato**2 - 8

izquierda = 2
derecha = 3

for vuelta in range(10):

    aproximacion = (izquierda + derecha) / 2

    if expresion(izquierda) * expresion(aproximacion) < 0:
        derecha = aproximacion
    else:
        izquierda = aproximacion

print(aproximacion)