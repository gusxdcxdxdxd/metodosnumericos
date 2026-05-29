def f(x):
    return x**3 - 2*x - 5

a = 2
b = 3

for i in range(10):
    c = (a + b)/2

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print(c)