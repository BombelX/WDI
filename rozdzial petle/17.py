
def silnia(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s
x = float(input("Podaj wartość x z cos(x) jaką chcesz obliczyć"))
n_max = 100
n = 1
res = 0
while n_max > n:
    res += (((-1)**n)/silnia(2*n))*(x**(2*n))
    n += 1
print(str(round((1+res),7))+"...")