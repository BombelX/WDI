
n = 5
tab = [[[""] for i in range(n)] for _ in range(n)]
tab[1][3][0] = tab[1][1][0]  = "/"

tab[3][0][0] = tab[3][3][0]  = tab[4][1][0] = tab[4][4][0] = "\\"


line = 0
row = 0
direction = 2 # 0 - w gore, 1 - w prawo,  2 - w dol,  3 - w lewo
path = [[0,0,0]]
flg = False

while True:
    if not flg:
        if direction == 0:
            line -=1
        elif direction == 1:
            row += 1
        elif direction == 2:
            line += 1
        else:
            row -= 1
        if line == (n-1) and row == (n-1):
            print("koniec ,sukces")
            break
    else:
        flg = False

    
    
    if line >= 0 and row >= 0  and line < n and row < n:
        if tab[line][row][0] =="\\":
            path.append([line,row,direction])
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 1
            else:
                direction = 0
        elif tab[line][row][0] =="/":
            path.append([line,row,direction])
            if direction == 0:
                direction = 1
            elif direction == 1:
                direction = 0
            elif direction == 2:
                direction = 3
            else:
                direction = 2
    else:
        print("tst")
        line , row , direction  = path[-1][0] , path[-1][1] ,path[-1][2]
        if tab[line][row][0] == "\\":
            tab[line][row][0] = "/"
        elif tab[line][row][0] == "/":
            tab[line][row][0] = "\\"
        print (line,row)
        flg = True
    
            
            
            
        
        
        