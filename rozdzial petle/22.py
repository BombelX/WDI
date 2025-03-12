#Zadanie 22. Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ...
# eps = int(input("Podaj dokładność (ile wykonac krokow) : "))

# def silnia(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#     return res
# e,index = 0,0
# e = duble
# while index < eps:
#     e += 1/silnia(index)
#     index += 1
# print(e)
     

from decimal import Decimal, getcontext
getcontext().prec = 35
def silnia(n):
    res = Decimal(1)
    for i in range(1, n + 1):
        res *= i
    return res
eps = int(input("Podaj dokładność (ile wykonać kroków): "))
e = Decimal(0)
for index in range(eps):
    e += Decimal(1) / silnia(index)
print(f"Liczba e z dokładnością do 30 miejsc po przecinku: {e:.30f}")
