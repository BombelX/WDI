import random
n = 100
tab = [0 for _ in range(n)]

for i in range(n):
    tab[i] = random.randrange(1,99,2)
    
    
max_len_with_positive_r = max_len_with_negativ_r = [0,0]

for i in range(n):
    last = tab[i]
    if i+1 < n:
        r = tab[i+1] - tab[i]
    len = 1
    for j in range(i+1,n):
        if j+1<n:
            if (tab[j+1] - tab[j]) == r:
                len += 1
            else:
                break        
        now = tab[j]
        
    if r > 0:
        if len > max_len_with_positive_r[0]:
            max_len_with_positive_r = [len,i]
    else:
        if len > max_len_with_negativ_r[0]:
            max_len_with_negativ_r = [len,i]
print(tab)
print(abs(max_len_with_positive_r[0]-max_len_with_negativ_r[0]))