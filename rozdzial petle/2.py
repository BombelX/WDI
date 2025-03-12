
max = 1000000
liczba = 1
last_num = 0
last_2num = 1
while liczba+last_2num + last_num < max:
    liczba = last_2num + last_num
    print(liczba)
    last_2num = last_num
    last_num = liczba   