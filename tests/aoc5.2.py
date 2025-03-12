with open("aoc5.txt","r") as file:
    lines = [line.rstrip() for line in file.readlines()]

size = len(lines)
main_tab = []
flag = True
start = (0,0)
for inx,line in enumerate(lines):
    main_tab.append(list(line))
    if flag:
        if "^" in line:
            start = (inx,line.index("^"))
            flag = False
pos = start
direction = "up"
flg1 = False
counter = 0
for i in range(size):
    print(i,size)
    for j in range(len(lines[0])):

        visited = []
        if main_tab[i][j] == "#":
            continue
        main_tab[i][j] = "#"
        pos = start
        direction = "up"
        flg1 = False

        while pos[0]>=0 and pos[1]>=0 and pos[0]< size and pos[1]<size:
            if [pos,direction] in visited:
                counter+=1
                break
            
            visited.append([pos,direction])


            flg1 = True

            # main_tab[pos[0]][pos[1]] = "X"
            if direction == "up":
                if pos[0]-1 >= 0 :
                    if main_tab[pos[0]-1][pos[1]] == "#":
                        direction = "right"
                    else:
                        pos = (pos[0]-1,pos[1])
                else:
                    break
            if direction == "right":
                if pos[1]+1<size:
                    if main_tab[pos[0]][pos[1]+1] == "#":
                        direction = "down"
                    else:
                        pos = (pos[0],pos[1]+1)
                else:
                    break
            if direction == "down":
                if pos[0]+1 < size:
                    if main_tab[pos[0]+1][pos[1]] == "#":
                        direction = "left"
                    else:
                        pos = (pos[0]+1,pos[1])
                else:
                    break
            if direction == "left":
                    if pos[1]-1>=0:
                        if main_tab[pos[0]][pos[1]-1] == "#":
                            direction = "up"
                        else:
                            pos = (pos[0],pos[1]-1)
                    else:
                        break
        main_tab[i][j] = "."

# print(*main_tab,sep="\n")

print(counter)