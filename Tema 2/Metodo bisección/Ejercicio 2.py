def f(x):
    return x**2 - 4

a = 0
b = 3

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)