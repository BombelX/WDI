import copy
from math import sqrt,log10
def king(w,k,board):
    res = False
    board_size = len(board)
    posible_moves = [(-1,-1),(-1,0),(-1,1),(0,1),(0,-1),(1,1),(1,0),(1,-1)]
    visited = [[] for _ in range(board_size*board_size)]
    def rek(w,k,visited,inx,last_digit):
        nonlocal res

        if res:
            return
        if [w,k] in [[0,0],[0,board_size-1],[board_size-1,0],[board_size-1,board_size-1]]:
            res = True
            return
        if 0 <= w < board_size and 0 <= k < board_size and [w,k] not in visited:
            if board[w][k]//10**(int(log10(board[w][k]))+1) != last_digit:
                return

            inx += 1
            visited[inx] = [w,k]
            for dx,dy in posible_moves:
                nx,ny = w+dx,k+dy
                rek(nx,ny,copy(visited),inx,board_size[w][k]%10)
        else:
            return
    rek(w,k,visited,0)
