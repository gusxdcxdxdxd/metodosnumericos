def funcion(valor):

    punto1 = 1
    dato1 = 2

    punto2 = 3
    dato2 = 6

    punto3 = 5
    dato3 = 18

    r1 = dato1 * ((valor - punto2)*(valor - punto3)) / ((punto1 - punto2)*(punto1 - punto3))
    r2 = dato2 * ((valor - punto1)*(valor - punto3)) / ((punto2 - punto1)*(punto2 - punto3))
    r3 = dato3 * ((valor - punto1)*(valor - punto2)) / ((punto3 - punto1)*(punto3 - punto2))

    return r1 + r2 + r3

print(funcion(4))