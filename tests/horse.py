posible_moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def horse(Tab, w, k, x=1):
    n = len(Tab)
    if 0 <= w < n and 0 <= k < n and Tab[w][k] == 0:
        Tab[w][k] = x
        if x == n * n:
            print(*Tab, sep="\n")
            print("------")
        else:
            for move in posible_moves:
                horse(Tab, w + move[0], k + move[1], x + 1)
        Tab[w][k] = 0
    else:
        return
size = 5
tb = [[0 for _ in range(size)] for _ in range(size)]
horse(tb, 0, 0)
