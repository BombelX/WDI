rok = 2024  # bieżący rok
def fibb(last_2num, last_num):
    liczba = last_2num + last_num
    while liczba < max_val:
        last_2num, last_num = last_num, liczba
        liczba = last_2num + last_num
        if liczba == rok:
            return True
    return False

for i in range(1, 10000):
    for j in range(i, 10000):  
        if fibb(i, j):
            print(f"Znaleziono rok przy liczbach poczatkowych {i}, {j}")
            break
