
tab = [12,3,4,34,2,12,143,2,4,8,16,32,64,2131233,213213,123,213,12324,324,32]
t_len = len(tab)

max_len = [0,0]

for i in range(t_len):
    last = tab[i]
    if i+1 < t_len:
        q = tab[i+1] / tab[i]
    len = 1
    for j in range(i+1,t_len):
        if j+1<t_len:
            if (tab[j+1] / tab[j]) == q:
                len += 1
            else:
                break        
        now = tab[j]
        

    if len > max_len[0]:
        max_len = [len,i]
print(max_len[0]+1,max_len[1]+1)
            