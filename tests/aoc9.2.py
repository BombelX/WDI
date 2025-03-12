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
                my_list += [[file_index,letter]]
                file_index+=1
            else:
                my_list += [["free-space",letter]]

    # while True:
    #     flag = False
    #     elem = my_list.pop(-1)
    #     if elem[0] == 'free-space':continue
    #     else:
    #         needed_space = elem[1]
    #         for inx,el in enumerate(my_list):
    #             if el[0] == "free-space" and el[1] >= needed_space:
    #                 flag = True
    #                 if el[1] - needed_space > 0 :
    #                     new_block = ["free-space",el[1] - needed_space]
    #                     my_list[inx] = elem
    #                     my_list.insert(inx+1,new_block)
    #                 else:
    #                     my_list[inx] = elem
    #                 break
    #         if not flag:
    #             my_list.append(elem)
    #             break 
    print(my_list)

    def repair():
        for inx, elem in enumerate(my_list):
            if elem[0] == "free-space":
                space = elem[1]
                for i, potential_elem in enumerate(reversed(my_list)):
                    if potential_elem[1] <= space and potential_elem[0] != "free-space":
                        tmp = my_list.pop(-i-1)
                        if space - tmp[1] > 0:
                            # Pozostała wolna przestrzeń
                            my_list[inx] = ["free-space", space - tmp[1]]
                            my_list.insert(inx, [tmp[0], tmp[1]])
                        else:
                            # Całkowicie zajęta przestrzeń
                            my_list[inx] = [tmp[0], tmp[1]]
                        repair()  # Kontynuuj rekurencję
                        return True
        return False

    # Wywołanie rekurencyjne
    while repair():
        pass


    print(my_list)

    index = 0
    summ = 0
    for part in my_list:
        if part[0] != "free-space":
            for i in range(index,index+part[1]):
                # print(str(i) + "*" + str(part[0]))
                summ += i*part[0]
            index += part[1]
    print(summ)



import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc
def pr(s):
    print(s)
    pc.copy(s)
sys.setrecursionlimit(10**6)
infile = sys.argv[1] if len(sys.argv)>=2 else 'aoc9.txt'
p1 = 0
p2 = 0
D = open(infile).read().strip()

def solve(part2):
    A = deque([])
    SPACE = deque([])
    file_id = 0
    FINAL = []
    pos = 0
    for i,c in enumerate(D):
        if i%2==0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            SPACE.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for (pos, sz, file_id) in reversed(A):
        for space_i,(space_pos, space_sz) in enumerate(SPACE):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos+i] == file_id, f'{FINAL[pos+i]=}'
                    FINAL[pos+i] = None
                    FINAL[space_pos+i] = file_id
                SPACE[space_i] = (space_pos + sz, space_sz-sz)
                break

    ans = 0
    for i,c in enumerate(FINAL):
        if c is not None:
            ans += i*c
    return ans

p2 = solve(True)
pr(p2)

                    

with open("aoc9.txt", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

def repair():
    for inx, elem in enumerate(my_list):
        if elem[0] == "free-space":
            space = elem[1]
            for i, potential_elem in enumerate(reversed(my_list)):
                if potential_elem[1] <= space and potential_elem[0] != "free-space":
                    tmp = my_list.pop(-i-1)
                    if space - tmp[1] > 0:
                        # Pozostała wolna przestrzeń
                        my_list[inx] = ["free-space", space - tmp[1]]
                        my_list.insert(inx, [tmp[0], tmp[1]])
                    else:
                        # Całkowicie zajęta przestrzeń
                        my_list[inx] = [tmp[0], tmp[1]]
                    repair()  # Kontynuuj rekurencję
                    return True
    return False

def generate_disk_map(my_list):
    disk_map = []
    for part in my_list:
        if part[0] == "free-space":
            disk_map.extend(["."] * part[1])  # Wolna przestrzeń
        else:
            disk_map.extend([str(part[0])] * part[1])  # ID pliku
    return "".join(disk_map)

for line in lines:
    my_list = []
    file_index = 0

    # Tworzenie listy plików i wolnej przestrzeni
    for index, letter in enumerate(line):
        letter = int(letter)
        if letter != 0:
            if index % 2 == 0:
                my_list.append([file_index, letter])  # Plik: ID, długość
                file_index += 1
            else:
                my_list.append(["free-space", letter])  # Wolna przestrzeń

    # Naprawa dysku
    while repair():
        pass

    # Generowanie końcowego stanu dysku
    final_disk_map = generate_disk_map(my_list)
    print(final_disk_map)


