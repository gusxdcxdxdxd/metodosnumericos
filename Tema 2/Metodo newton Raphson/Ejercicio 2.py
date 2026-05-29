def ecuacion(numero):
    return numero**2 - 9

def pendiente(numero):
    return 2 * numero

valor = 4

for i in range(6):
    valor = valor - ecuacion(valor) / pendiente(valor)

print(valor)