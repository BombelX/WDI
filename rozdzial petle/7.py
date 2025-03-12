eps = 8e-2
s = int(input("Podaj liczbe ktorej przyblizenie pierwiastka 3 stopnia chcesz uzyskać: "))
a = s
b = 1


while abs(2*a-2*b) >= eps: 
    a = (a+2*b)/3
    b = (s/a**2)
print(a)