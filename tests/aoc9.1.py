with open("aoc9.txt","r") as file:
    lines = [line.rstrip() for line in file.readlines()]
summ = 0

for line in lines:
    my_list = []
    file_index = 0
    for index,letter in enumerate(line):
        letter = int(letter)
        if letter != 0:
            if index%2 == 0:
                my_list += [str(file_index)]*letter
                file_index+=1
            else:
                my_list += ['.']*letter
    size = len(my_list)

    for i,k in enumerate(my_list):
        if my_list[i] == ".":
            x = size-1
            while x > i:
                x -= 1
                num = my_list.pop(-1)
                size -=1
                if num != ".":
                    my_list[i] = num
                    break
    part_sum = 0
    for multiplayer,elem in enumerate(my_list):
        if elem != ".":
            part_sum += int(elem)*multiplayer
    summ+=part_sum
print(summ)