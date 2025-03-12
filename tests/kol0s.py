
def king(N,L):
    max_path = 0
    board_size = N
    posible_moves = [(0,-1),(1,0),(0,1),(-1,0)]
    def rek(w,k,visited,path):
        nonlocal max_path
        if w == board_size-1 and k == board_size-1:
            max_path = max(max_path,path)
            return
        if [w,k] in visited:
            return
        for dx,dy in posible_moves:
            nx,ny = w+dx,k+dy
            if 0<=nx<board_size and 0<=ny<board_size and (nx,ny) not in L:
                n_visited = [x for x in visited]
                n_visited[path] = [w,k]
                rek(nx,ny,n_visited,path+1)
    rek(0,0,[[] for _ in range(board_size**2)],0)
    return max_path

N = 5
L=[(0,1),(4,0),(1,2),(4,3),(3,0),(1,3)]

# print(king(N,L))


def king_bctrc(N,L):
    board_size = N
    max_path = 0
    posible_moves = [(0,-1),(1,0),(0,1),(-1,0)]
    def rek(w,k,path,visited):
        nonlocal max_path
        if w == N-1 and k == N-1:
            max_path = max(max_path,path)
            return
        if [w,k] in visited:
            return
        for dx,dy in posible_moves:
            nx,ny = w+dx,k+dy
            if 0<=nx<board_size and 0<=ny<board_size and (nx,ny) not in L:
                visited[path] = [w,k]
                rek(nx,ny,path+1,visited)
                visited[path+1] = [0,0]
    rek(0,0,0,[[] for _ in range(N**2+1)])
    return max_path

# print(king_bctrc(N,L))

def only2_prime_factors(n):
    check_tab = [False,False]
    div = 2
    while n>1:
        if n%div == 0:
            if check_tab[0]== False:
                check_tab[0] = True
            elif check_tab[1] == False:
                check_tab[1] = True
            else:
                return False
            n//=div
            div = 2
        else:
            div +=1
    if check_tab[0] == True and check_tab[1] == True:
        return True
    else:
        return False

def square(T):
    size = len(T)
    for square_size in range(2,size):
        for x in range(0,size-square_size):
            for y in range(0,size-square_size):
                n = T[x][y]*T[x+square_size][y]*T[x][y+square_size]*T[x+square_size][y+square_size]#lewy gorny,prawy gorny,prawy donly ,lewy dolny
                if only2_prime_factors(n):
                    return square_size
                else:
                    continue
    return 0





