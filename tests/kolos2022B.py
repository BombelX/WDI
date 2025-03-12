x = [2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]
r = []

def is_growing(start, end, tab):
    if end - start < 2:  
        return False
    tb = [tab[start]]  
    for i in range(start + 1, end + 1):
        if tab[i - 1] >= tab[i]:  
            return False
        tb.append(tab[i])
    r.append(tb.copy())  
    return True

def sequence(tab):
    dl = len(tab)
    for start in range(dl):
        for end in range(start + 1, dl): 
            is_growing(start, end, tab)


