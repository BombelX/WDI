from copy import deepcopy

with open("aoc7.txt","r") as file:
    lines = [line.rstrip().split(":") for line in file.readlines()]


def check_possible_equations(target, actual_res, remaining_values):
    global flag
    if len(remaining_values) == 0:
        if actual_res == target:
            flag = True
        return
    variable = remaining_values.pop(0)
    if actual_res == 0:
        check_possible_equations(target,variable,deepcopy(remaining_values))
    else:
        check_possible_equations(target,actual_res*variable,deepcopy(remaining_values))
        check_possible_equations(target,actual_res+variable,deepcopy(remaining_values))
        check_possible_equations(target,int(f"{actual_res}"+f"{variable}"),deepcopy(remaining_values))

summ = 0
for line in lines :
    target = int(line[0])
    values = [int(elem) for elem in line[1].split(" ")[1:]]
    flag = False
    check_possible_equations(target,0,values)
    if flag:
        summ+=target
print(summ)