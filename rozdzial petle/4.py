maxsum = int(input("podaj maxsume: "))
def fibb(last_2num, last_num):
    suma = 0
    liczba = last_2num + last_num
    while liczba < maxsum:
        last_2num, last_num = last_num, liczba
        liczba = last_2num + last_num
        if liczba > maxsum:
            return False
        suma += liczba
        if suma == maxsum:
            print(suma)
            return True

        
    return False

for i in range(1, 10000):
    for j in range(i, 10000):  
        if fibb(i, j):
            print(f"Znaleziono rok przy liczbach poczatkowych {i}, {j}")
            break
        break
print("nie iestneije")