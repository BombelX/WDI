with open("aoc5.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

size = len(lines)
main_tab = set()  # Zbiór przechowujący współrzędne pozycji z "#"
start = (0, 0)

for inx, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            main_tab.add((inx, j))
        elif char == "^":
            start = (inx, j)

pos = start
direction = "up"
counter = 0

for i in range(size):
    for j in range(len(lines[0])):
        if (i, j) in main_tab:  # Sprawdź, czy komórka to "#"
            continue
        main_tab.add((i, j))  # Tymczasowo ustaw jako "#"
        pos = start
        direction = "up"
        visited = set()  # Zestaw odwiedzonych stanów

        while 0 <= pos[0] < size and 0 <= pos[1] < size:
            current_state = (pos, direction)
            if current_state in visited:
                counter += 1
                break

            visited.add(current_state)

            # Poruszanie się w kierunku
            if direction == "up":
                next_pos = (pos[0] - 1, pos[1])
                if next_pos in main_tab:  # Jeśli ściana, zmiana kierunku
                    direction = "right"
                elif next_pos[0] >= 0:
                    pos = next_pos
                else:
                    break
            elif direction == "right":
                next_pos = (pos[0], pos[1] + 1)
                if next_pos in main_tab:
                    direction = "down"
                elif next_pos[1] < size:
                    pos = next_pos
                else:
                    break
            elif direction == "down":
                next_pos = (pos[0] + 1, pos[1])
                if next_pos in main_tab:
                    direction = "left"
                elif next_pos[0] < size:
                    pos = next_pos
                else:
                    break
            elif direction == "left":
                next_pos = (pos[0], pos[1] - 1)
                if next_pos in main_tab:
                    direction = "up"
                elif next_pos[1] >= 0:
                    pos = next_pos
                else:
                    break

        main_tab.remove((i, j))  # Przywróć na "." po zakończeniu sprawdzania

print(counter)
with open("res.txt","w") as f:
    f.write(counter) 