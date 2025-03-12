sprawdz = int(input("podaj liczbe ktora chcesz sprawdzic"))

max = 10e10
liczba = 1
elements = []
last_num = 0
last_2num = 1
while liczba+last_2num + last_num < max:
    liczba = last_2num + last_num
    elements.append(liczba)
    last_2num = last_num
    last_num = liczba   
for i in range(len(elements)) :
    if (elements[i]*elements[i+1]) == sprawdz :
        print("istnieje")
        break
    else:
        if elements[i+1] > sprawdz:
            print("nie istnieje")
            break
    