def ecuacion(numero):
    return 4 * numero - 5

x0 = 1
paso = 0.05

resultado = (
    ecuacion(x0 + paso)
    - ecuacion(x0 - paso)
) / (2 * paso)

print(resultado)