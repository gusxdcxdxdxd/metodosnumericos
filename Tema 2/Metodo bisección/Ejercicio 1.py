def f(x):
    return x**3 - x - 2

a = 1
b = 2

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)