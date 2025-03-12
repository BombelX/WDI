inp = ""
tab = [0 for x in range(99999)]
inx = 0
while inp != "0" :
    inp = input("Podaj liczbę: ")
    tab[inx] = int(inp)
    inx += 1
tab_good = [x for x in tab[:tab.index(0)]] #Pozbywamy sie niepotrzebnych zer z tabliy aby niemarnowac pamieci oraz mocy obliczeniwoej, iterujemy od pierwszego elementu do pierwszego wystapienia 0
tab = [0 for i in range(inx)] # zwalniamy pamieć
maxindex = 0
print(tab_good)
for i in range(0,inx):
    max = 0
    for x in range(inx-1):
        if tab_good[x] > max:
            maxindex = x
            max = tab_good[x]
    
    tab[i] = max
    tab_good[maxindex] = 0
print(tab[10])
        
        
        
    