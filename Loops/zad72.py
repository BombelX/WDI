import random
size = 100
tab = [random.randrange(100,999) for _ in range(size)]
# tab = [2,9,3,1,7,5,6,11,9,6,7,6,5,7,1,3,9,12,15]
def is_subsqn_rvs(sub_seq,end,len):
    sub = [0 for _ in range(0,len)]
    index = 0
    for el in sub_seq:
        sub[len-index-1] = el
        index += 1
    for i in range(end+1,size):
        if tab[i] == sub[0]:
            if len == 1:
                return True
            pos = 1
            flg = True
            if i+len <= size:
                for x in range(i+1,i+len):
                    if tab[x] != sub[pos]:
                        flg = False
                        break
                    pos += 1
                if flg:
                    return True
    return False
                    
                    
            

        

maxlen = 0
for start in range(size):
    for end in range(start,size):
        sub_seq = tab[start:end+1]
        len = end+1-start
        if not is_subsqn_rvs(sub_seq,end,len):
            if len > maxlen:
                maxlen = len-1
            break
print(maxlen)