inicio_x = 3
inicio_y = 7

fin_x = 9
fin_y = 25

objetivo = 6

respuesta = inicio_y + (
    (fin_y - inicio_y)
    / (fin_x - inicio_x)
) * (objetivo - inicio_x)

print(respuesta)