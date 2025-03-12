board = [['W', '.', '.', '.', '.', '.', '.', '.'],
    ['.', 'W', '.', '.', '.', '.', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'W', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', '.', '.', '.', '.', 'W']]

def znajdz_wieze(board):
    row_rooksum = [0]*8
    col_rook_sum = [0]*8
    for x in range (len(board)):
        for y in range(len(board)):
            if board[x][y] == "W":
                row_rooksum[x] += 1
                col_rook_sum[y] +=1
    bad_row = 0
    good_row = 0
    for x in range(len(row_rooksum)):
        if row_rooksum[x] == 0 :
            good_row = x
        elif row_rooksum[x] != 1 :
            
            bad_row = x
        else:
            continue
    bad_col = 0
    good_col = 0
    for x in range(len(col_rook_sum)):
        if col_rook_sum[x] == 0 :
            good_col = x
        elif col_rook_sum[x] != 1 :
            bad_col = x
        else:
            continue
    return [(bad_row,bad_col),(good_row,good_col)]

print(znajdz_wieze(board))