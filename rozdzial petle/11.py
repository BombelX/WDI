import math 
liczba = int(input("podaj liczbe ktorej liste dzielnikow chesz uzyskać"))
podzielniki = []
for i in range (1,math.ceil(liczba/2)+1):
    if liczba%i == 0:
        podzielniki.append(i)
print(podzielniki)
    