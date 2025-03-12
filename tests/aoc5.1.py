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
while pos[0]>=0 and pos[1]>=0 and pos[0]< size and pos[1]<size:
    main_tab[pos[0]][pos[1]] = "X"
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
# print(*main_tab,sep="\n")

cnt = 0

for line in main_tab:
    for x in line:
        if x == "X":
            cnt+=1
print(cnt)
