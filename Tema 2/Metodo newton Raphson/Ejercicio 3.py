def formula(dato):
    return dato**2 - 5

def cambio(dato):
    return 2 * dato

inicio = 2

for vuelta in range(7):
    inicio = inicio - formula(inicio) / cambio(inicio)

print(inicio)