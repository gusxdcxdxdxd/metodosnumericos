def formula(dato):
    return dato**2 - 4*dato + 1

centro = 3
delta = 0.1

respuesta = (
    formula(centro + delta)
    - formula(centro - delta)
) / (2 * delta)

print(respuesta)