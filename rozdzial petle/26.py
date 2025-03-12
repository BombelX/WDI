
from decimal import Decimal, getcontext
getcontext().prec = 100
a = int(input("Podaj a: "))
b = int(input("Podaj b:"))
n = int(input("Podaj n: "))
print(f"{a/b:.{n}f}")