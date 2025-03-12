tab = [
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
     ]
min_len = 9999
tab_size = len(tab)
def jump(pos_x,pos_y,n):
    if pos_x >= 0 and pos_x < tab_size and pos_y < tab_size and pos_y >=0:
        if tab[pos_x][pos_y] == 0:
            global min_len
            if pos_x == (tab_size-1):
                min_len = min(n,min_len)
                return
            else:
                jump(pos_x+2,pos_y+1,n+1)
                jump(pos_x+2,pos_y-1,n+1)
                jump(pos_x+1,pos_y+2,n+1)
                jump(pos_x+2,pos_y-2,n+1)
        else:
            return
    else:
        return
for i in range(tab_size):
    jump(0,i,0)
print(min_len)


