from copy import deepcopy
from itertools import combinations
from math import ceil


with open("aoc8.txt","r") as file:
    lines = [list(line.rstrip()) for line in file.readlines()]

size = len(lines[0])
dict = {}

for x,line in enumerate(lines):
    for y,elem in enumerate(line):
        if elem != ".":
            if not elem in dict:
                dict[elem] = [(x,y)]
            else:
                dict[elem].append((x,y))

antenodes_list = []
for antena in dict:
    antens = list(combinations(dict[antena],2))
    for ant_pairs in antens:
        distx = abs(ant_pairs[0][0] - ant_pairs[1][0]) -1
        disty = abs(ant_pairs[0][1] - ant_pairs[1][1]) -1
        if size > ant_pairs[0][1]+disty and size > ant_pairs[0][0]+distx:
            antenodes_list.append((ant_pairs[0][0]+distx,ant_pairs[0][1]+disty)) 
        if  0 <= ant_pairs[0][1]-disty and 0 <= ant_pairs[0][0]-distx:
            antenodes_list.append((ant_pairs[0][0]-distx,ant_pairs[0][1]-disty)) 
antenodes_list = set(antenodes_list)
print (len(antenodes_list))

