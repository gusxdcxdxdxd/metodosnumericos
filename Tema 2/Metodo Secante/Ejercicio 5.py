def formula(valor):
    return valor**3 - valor - 7

a = 2
b = 3

for ciclo in range(10):

    resultado = (a + b) / 2

    if formula(a) * formula(resultado) < 0:
        b = resultado
    else:
        a = resultado

print(resultado)