a = 0
b = 0

for vuelta in range(15):

    siguiente_a = (14 - 2*b) / 5
    siguiente_b = (11 - a) / 4

    a = siguiente_a
    b = siguiente_b

print(a, b)