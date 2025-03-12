import math
def convert_to_base4(n):
    '''Funkcja ma na celu konwersje liczby z systemu 10-tnego na 4-kowy'''
    dl = 0
    tab = [0 for _ in range(64)]

    while n>0:
        tab[dl] = n%4
        n //= 4
        dl+=1
    res = [0 for _ in range(dl)]
    i = 0
    for x in range(0,dl):
        res[x] = tab [dl-x-1]
        i+=1
    return res,dl

def has_same_digits(tab_b10,tab_b4,dl_b10,dl_b4):
    ch_tab = [False for _ in range(10)]

    for i in range(dl_b10):
        ch_tab[tab_b10[i]] = True
    for j in range(dl_b4):
        ch_tab[tab_b4[j]] = False

    for x in range(10):
        if ch_tab[x]:
            return False
    return True

def find_consistent_sub_sequence(tab):
    l_tab = len(tab)
    maxlen = 0
    seq_len = 0
    for i in range(l_tab):
        b4,b4_dl = convert_to_base4(tab[i]) 
        b10_dl = int(math.log10(l_tab))+1
        b10 = [0]*(b10_dl+1)
        tmp = tab[i]
        inx = 0
        while tmp>0:
            b10[inx] = tmp%10
            tmp //= 10
            inx +=1
        if has_same_digits(b10,b4,b10_dl,b4_dl):
            seq_len+=1
        else:
            maxlen = max(seq_len,maxlen)
            seq_len = 0
    return  maxlen
print(find_consistent_sub_sequence([13,18,107,23,21,9]))

    

        
    