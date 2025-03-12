def minimalization(machine):
    from collections import deque
    # Inicjalizacja kolejki BFS
    queue = deque([(0, 0, 0)])  # (koszt, posx, posy)
    visited = set()  # Zbiór odwiedzonych pozycji
    visited.add((0, 0))

    coin_min = float("inf")

    while queue:
        cost, posx, posy = queue.popleft()

        # Jeśli osiągnęliśmy cel, zaktualizuj minimalny koszt
        if posx == machine[4] and posy == machine[5]:
            coin_min = min(coin_min, cost)
            continue

        # Rozważ naciśnięcie przycisku A
        next_pos_a = (posx + machine[0], posy + machine[1])
        if next_pos_a not in visited and posx + machine[0] <= machine[4] and posy + machine[1] <= machine[5]:
            visited.add(next_pos_a)
            queue.append((cost + 3, *next_pos_a))

        # Rozważ naciśnięcie przycisku B
        next_pos_b = (posx + machine[2], posy + machine[3])
        if next_pos_b not in visited and posx + machine[2] <= machine[4] and posy + machine[3] <= machine[5]:
            visited.add(next_pos_b)
            queue.append((cost + 1, *next_pos_b))

    return coin_min if coin_min != float("inf") else -1  # Jeśli brak rozwiązania, zwróć -1


# Wczytaj dane i wykonaj obliczenia
with open("aoc13.txt", "r") as file:
    lines = file.readlines()

index = 0
tab = []
tmp = [0, 0, 0, 0, 0, 0]
for line in lines:
    if line == "\n":
        index += 1
        tab.append(tmp)
        tmp = [0, 0, 0, 0, 0, 0]

    elif "Button" in line:
        tm = line.split(",")
        dx, dy = int(tm[0].split("+")[1]), int(tm[1].split("+")[1])
        if "A" in line:
            tmp[0] = dx
            tmp[1] = dy
        else:
            tmp[2] = dx
            tmp[3] = dy
    else:
        tmp[4] = int(line.split(",")[0].split("=")[1])
        tmp[5] = int(line.split(",")[1].split("=")[1])
summ = 0
for machine in tab:
    tmp = minimalization(machine)
    if tmp != -1:
        summ+=tmp
print(summ)