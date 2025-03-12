with open("aoc12.txt","r") as file:
    lines = [list(line.rstrip()) for line in file.readlines()]
moves = {(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)}
plants_set = {}
for x,line in enumerate(lines):
    for y,plant in enumerate(line):
        if plant not in plants_set:
            plants_set[plant] = [1,0]
        else:
            plants_set[plant][0] +=1
        for dx,dy in moves
        
