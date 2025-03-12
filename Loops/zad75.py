tab = [1,1,1,1,1,1,12,16,20,23,27,30,40,60,60,60,60,60,23,23,123,1123,4343,54,23,123,55,66,33,334,40,230,600,3430,12312,34305,23456,2346,9586,43804,4938,48592,48403,999999,999999,999999,999999]

max = 0
min = 99999999999

for elem in tab:
    if elem > max:
        max = elem
    if elem < min:
        min = elem
cntmin,cntmax = 0,0

for elem in tab:
    if elem == max:
        cntmax += 1
    if elem == min:
        cntmin += 1    
if cntmin > 1:
    print("Nie ma najwiekszego")
if cntmax > 1:
    print("Nie ma najwiekszego")