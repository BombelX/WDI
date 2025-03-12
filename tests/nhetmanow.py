def Is_Safe(hetmans_pos,act_col):
    x = len(hetmans_pos)
    y = act_col

    for row,col in enumerate(hetmans_pos):
        if col == y:
            return  False
        if abs(row-x) == abs(col-y):
            return False
    return True
def set_Hetman(hetmans_pos,n):
    if len(hetmans_pos) == n:
        print(hetmans_pos)
        return
    for i in range(n):
        if Is_Safe(hetmans_pos,i):
            set_Hetman(hetmans_pos+[i],n)

set_Hetman([],12)