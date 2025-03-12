def validate(T):
    for x in range(len(T)):
        col_val = [False] * 10
        row_val = [False] * 10
        for y in range(len(T)):
            col_val[T[x][y]] = True
            row_val[T[y][x]] = True
        if False in row_val[1:] or False in col_val[1:]:
            return False
    return True

def swap(s1, s2, T):
    # Naprawione indeksowanie dla poprawnego zakresu (od 1 do 9)
    row_start1 = (s1 - 1) // 3 * 3
    row_start2 = (s2 - 1) // 3 * 3
    col_start1 = (s1 - 1) % 3 * 3
    col_start2 = (s2 - 1) % 3 * 3
    for x in range(3):
        for y in range(3):
            # Zamiana elementów między dwoma małymi kwadratami
            T[row_start1 + x][col_start1 + y], T[row_start2 + x][col_start2 + y] = (
                T[row_start2 + x][col_start2 + y],
                T[row_start1 + x][col_start1 + y],
            )
    return T

def sudoku(T):
    for sqr1 in range(1, 10):  # Indeksowanie od 1 do 9
        for sqr2 in range(1, 10):
            if sqr1 == sqr2:
                continue
            # Zamiana małych kwadratów
            swap(sqr1, sqr2, T)
            if validate(T):
                return (sqr1, sqr2)
            # Przywrócenie poprzedniego stanu
            swap(sqr1, sqr2, T)

# Testowanie
T = [
    [8, 1, 2, 7, 5, 3, 6, 4, 9],
    [9, 4, 3, 6, 8, 2, 1, 7, 5],
    [6, 7, 5, 4, 9, 1, 2, 8, 3],
    [1, 5, 4, 3, 6, 8, 8, 9, 6],
    [3, 6, 9, 9, 1, 7, 7, 2, 1],
    [2, 8, 7, 4, 5, 2, 5, 3, 4],
    [5, 2, 1, 9, 7, 4, 2, 3, 7],
    [4, 3, 8, 5, 2, 6, 8, 4, 5],
    [7, 9, 6, 3, 1, 8, 1, 6, 9],
]

print(sudoku(T))  # Output: (5, 9)
