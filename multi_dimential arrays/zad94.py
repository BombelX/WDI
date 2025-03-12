tab1 = [
    [79, 2, 3, 5, 7, 9, 11],
    [2, 4, 6, 8, 10, 12, 14],
    [3, 6, 9, 12, 15, 18, 21],
    [4, 8, 12, 16, 20, 24, 28],
    [5, 10, 15, 20, 25, 30, 35],
    [7, 14, 21, 28, 35, 42, 49],
    [11, 22, 33, 44, 55, 66, 77]
]
t2 = []

frame = [0,0,0,0,0,0,0]
f= True
while f :
    min = tab1[0][frame[0]]
    minindex = 0
    for index in range(len(frame)):
        if frame[index] < len(tab1[0]):
            if min > tab1[index][frame[index]]:
                minindex = index
                min = tab1[index][frame[index]]
    t2.append(min)
    frame[minindex] +=1
    f1 = True
    for i in range(1,7):
        if frame[i] < len(frame):
            f1 = False
    if f1 == True:
        f = False

print(t2)
    