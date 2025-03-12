def NWD(a,b):
    while a%b != 0:
        a,b = b,a%b
    return b
    

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbę: "))

print(NWD(NWD(a,b),c))
