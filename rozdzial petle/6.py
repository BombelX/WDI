eps = 1e-100
s = int(input("Podaj liczbe ktorej przyblizenie pierwiastka chcesz uzyskać: "))
a = 0
an = 1
while abs(an-a) >= eps:
    a = an
    an = ((s/an)+an)/2
print(a)