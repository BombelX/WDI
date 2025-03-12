
def is_neg_palindrom(tab,i,j):
    for k in range(j-i):
        if tab[i+k]%2 == 0 and tab[i+k] != tab[j-k]: return False
    return True





def the_longest_palindrom(tab):
    max_len = 0
    for x in range(len(tab)):
        if tab[x] % 2 == 1:
            for i in range((x+1,len(tab))):
                if is_neg_palindrom(tab,x,i):
                    max_len = max(max_len,i-x+1)

    return max_len