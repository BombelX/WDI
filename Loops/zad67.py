import math 
tab = [10, 2, 1, 0, 0, 5, 0, 0, 0, 0, 1]

tab_len = len(tab)-1


def find_prime_dividers(elem):
    divs = [0 for _ in range(elem)]
    index_of_prime = 0
    inx_of_div = 0
    f_divs = [0 for _ in range(elem)]
    
    
    for x in range(2,elem+1):
        if elem % x == 0 :
            divs[inx_of_div] = x
            inx_of_div +=1
    divs = [div for div in divs[:divs.index(0)]]
    for div in divs:
        flg = True
        if (div%2) != 0 or div == 2:
            for i in range(2,math.ceil(math.sqrt(div))):
                if div % i == 0:
                    flg = False
                    break
            if flg:
                f_divs[index_of_prime] = div
                index_of_prime += 1
        else:
            continue
    res = []
    if index_of_prime != 0:     
        res = [n for n in f_divs[:f_divs.index(0)]]
    return res
            
def rec_find(start,tab):
    tb = find_prime_dividers(tab[start])
    for div in tb:
        if (start+div) > tab_len:
            return False
        if div+start == tab_len:
            return True
        if rec_find(div+start,tab) == True:
            print("Znaleziono")
            break 
        
        
rec_find(0,tab)
