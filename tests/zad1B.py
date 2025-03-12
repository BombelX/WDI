sudoku = [ [8,1,2,7,5,3,6,4,9]
          ,[9,4,3,6,8,2,1,7,5]
          ,[6,7,5,4,9,1,2,8,3]
          ,[1,5,4,3,6,8,8,9,6]
          ,[3,6,9,9,1,7,7,2,1]
          ,[2,8,7,4,5,2,5,3,4]
          ,[5,2,1,9,7,4,2,3,7]
          ,[4,3,8,5,2,6,8,4,5]
          ,[7,9,6,3,1,8,1,6,9]]

line_cnt = 0
row_cnt = 0

sqr_line_check = [True,True,True]
sqr_row_check = [True,True,True]

for line in sudoku:
    tab = [0 for _ in range(9)]
    for elem in line:
        tab[elem-1] += 1
    if min(tab) != 1 and max(tab) != 1:
        if line_cnt <=2:
            sqr_line_check[0] = False
        elif line_cnt <= 5:
            sqr_line_check[1] = False
        else:
            sqr_line_check[2] = False            
    line_cnt+=1
for row in range(9):
    tab = [0 for _ in range(9)]
    for x in range(9):
        tab[sudoku[row][x]-1] +=1 
    if min(tab) != 1 and max(tab) != 1:
        if row_cnt <=2:
            sqr_row_check[0] = False
        elif row_cnt <= 5:
            sqr_row_check[1] = False
        else:
            sqr_row_check[2] = False
    row_cnt += 1
print(sqr_row_check)
print(sqr_line_check)





