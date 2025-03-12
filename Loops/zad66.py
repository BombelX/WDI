import random

tab_size = int(input("Podaj jak duza ma byc tablica :"))
tab = [0 for _ in range(tab_size)]
for i in range(tab_size):
    rand = int(random.random()*1000)
    rand_chck = rand
    tmp = True
    tab[i] = rand
    while rand_chck != 0 :
        if ((rand_chck%10) % 2) == 0:
            tmp = False
            break
        rand_chck //= 10
    if tmp :
        print("Tak istnieje liczba w ciagu zlozona tylko z liczb nieparzystych")
        break
if not tmp:
    print("NIe nie istenieje zadna liczba w tym ciagu ktora jest utworzona tylko z liczb nieparzystych")
print(tab)