
# def Is_safe(hetmans_pos, act_col):
#     x = len(str(hetmans_pos))  
#     y = act_col              
    
#     for i in range(x):  
#         prev_col = (hetmans_pos // 10**i) % 10  
#         prev_row = x - i - 1             
        
#         if prev_col == y:
#             return False

#         if abs(prev_row - x) == abs(prev_col - y):
#             return False
    
#     return True



# def SetHetman(pos,n):
    
#     if len(str(pos)) == n:
#         print(pos)
#         return
    
#     for i in range(n):
#         if Is_safe(pos,i):
#             SetHetman(pos*10+i,n)
#     return       
    

# SetHetman(0,10)

def Is_safe(hetmans_pos, act_col):
    x = len(hetmans_pos)
    y = act_col
    
    for row, col in enumerate(hetmans_pos):
        if col == y:
            return False
        if abs(row - x) == abs(col - y):
            return False

    return True

def SetHetman(hetmans_pos, n):
    if len(hetmans_pos) == n:
        print(hetmans_pos) 
        return
    
    for i in range(n):
        if Is_safe(hetmans_pos, i):
            SetHetman(hetmans_pos + [i], n)

SetHetman([],12)
