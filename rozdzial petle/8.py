import math

start = 2024
a = 0  # start with a non-negative value for c
b = 10
eps = 0.0000000001
c = 1
f = 1

while abs(f) >= eps:
    c = (a + b) / 2
    f = c**c - 2024
    if f > 0:
        b = c
    else:
        a = c

print(c)
