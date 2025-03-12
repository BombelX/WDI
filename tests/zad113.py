# import numpy as np

# N = 1000
# unique_rows = set()
# T_unique = []
# def generate_unique_row():
#     while True:
#         row = tuple(np.random.choice([0, 1], size=N))
#         if row not in unique_rows:
#             unique_rows.add(row)
#             return row

# for _ in range(N):
#     T_unique.append(generate_unique_row())

# T_unique_array = np.array(T_unique)

# tab = [0]*1000

# def bin_to_decimal(row):
#     num = 0
#     for x in range(1000):
#         num += row[x]* 2**x
#     return num

# for inx , row in enumerate(T_unique_array):
#     tab[inx] = bin_to_decimal(row)


# print(abs(tab.index(max(tab))-tab.index(max(tab))))

import numpy as np

N = 1000
unique_rows = set()
T_unique = []

# Generowanie unikalnych wierszy
def generate_unique_row():
    while True:
        row = tuple(np.random.choice([0, 1], size=N))
        if row not in unique_rows:
            unique_rows.add(row)
            return row

for _ in range(N):
    T_unique.append(generate_unique_row())

T_unique_array = np.array(T_unique)

# Funkcja do znalezienia odległości między wierszami o największej różnicy
def find_max_distance(T):
    # Inicjalizujemy wiersz minimalny i maksymalny jako pierwszy wiersz
    max_row = min_row = tuple(T[0])  # Konwertujemy wiersz na krotkę dla poprawnego porównania
    max_index = min_index = 0
    
    for i in range(1, len(T)):
        row_tuple = tuple(T[i])  # Konwersja na krotkę
        if row_tuple > max_row:  # Porównanie leksykograficzne
            max_row = row_tuple
            max_index = i
        elif row_tuple < min_row:
            min_row = row_tuple
            min_index = i
    
    return abs(max_index - min_index)

# Znalezienie maksymalnej odległości
distance = find_max_distance(T_unique_array)
print(distance)
