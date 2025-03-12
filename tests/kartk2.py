tab = [3, 7, 2, 4, 5, 10, 12, 5, 7, 8, 1, 2, 3, 15, 6, 4, 8, 19, 11, 5]
n = 20
max_len = 0

def is_growing(start,end,tab):
    last = tab[start]
    sum = last
    for inx in range(start+1,end):
        now = tab[inx]
        if now <= last:
            return 0
        sum += now
        last = now
    return sum
        
for start in range(n):
    for end in range(start+1,n+1):
        sum = is_growing(start,end,tab)
        if sum != 0:
            if ((start+end-1)/2)*(end-start) == sum:
                max_len = max(max_len,end-start)
print(max_len)
