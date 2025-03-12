import itertools

with open("aoc8.txt","r") as f:
    input_text = [line.rstrip('\n') for line in f.readlines()]

map_size = (len(input_text[0]), len(input_text))
points = {}

for y in range(len(input_text)):
    for x in range(len(input_text[y])):
        if input_text[y][x] != '.':
            point = (x, y)
            if input_text[y][x] not in points.keys():
                points[input_text[y][x]] = []
            points[input_text[y][x]].append(point)

antinodes_locations = []
for key, value in points.items():
    for a, b in itertools.permutations(value, 2):
        x_dif = a[0] - b[0]
        y_dif = a[1] - b[1]
        antinode = [a[0] + x_dif, a[1] + y_dif]
        if antinode[0] >= 0 and antinode[0] < map_size[0] and antinode[1] >= 0 and antinode[1] < map_size[1]:
            if antinode not in antinodes_locations:
                antinodes_locations.append((antinode[0],antinode[1]))

print(len(antinodes_locations))