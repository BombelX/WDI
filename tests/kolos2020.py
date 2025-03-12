T = ["ABAB", "XYZXYZXYZ", "AA", "ABCABCABCABC", "ABCDE"]
lenT = len(T)

def multi(tab,len_tab):
    max_len = 0
    for i in range(len_tab):
        el_len = len(tab[i])
        for part_len in range(1,el_len//2+1):
            pattern = [""]*part_len
            for x in range(part_len):
                pattern[x] = tab[i][x]
            flag = True
            for elem in range(part_len+1,el_len,part_len):
                inx = 0
                for f in range(elem-1,elem+part_len-1):
                    if pattern[inx] != tab[i][f]:
                        flag = False
                        break
                    inx +=1
                if not flag:
                    break
            if flag :
                max_len = max(max_len,el_len)
                break
    return max_len
    
print(multi(T,lenT))
