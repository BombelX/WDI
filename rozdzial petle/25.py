a = int(input("Podaj liczbę do sprawdzenia"))
fibb = []
max = 1000000
liczba = 1
last_num = 0
last_2num = 1
while liczba+last_2num + last_num < max:
    liczba = last_2num + last_num
    fibb.append(liczba)
    last_2num = last_num
    last_num = liczba   
print(fibb)

for f1 in fibb:
    if f1 > f2:
        break
    for f2 in fibb:
        if f2 > a:
            break
        if (f1*f2) == a:
            print("Istnieje") 