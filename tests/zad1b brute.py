sudoku_fi = [ 8,1,2,7,5,3,6,4,9
          ,9,4,3,6,8,2,1,7,5
          ,6,7,5,4,9,1,2,8,3
          ,1,5,4,3,6,8,8,9,6
          ,3,6,9,9,1,7,7,2,1
          ,2,8,7,4,5,2,5,3,4
          ,5,2,1,9,7,4,2,3,7
          ,4,3,8,5,2,6,8,4,5
          ,7,9,6,3,1,8,1,6,9]
lines = []
rows = [[],[],[]]
for i in range(27):
    t = []
    for j in range(3):
        t.append(sudoku_fi[i*3+j])
    lines.append(t)
inx = 0
for line in lines:
    rows[inx%3].append(line)
    inx +=1
sqr = [[] for _ in range(9)]
index = 0
for row in rows:
    n = 0
    for line in row:
        print(line)
        sqr[n//3+index*3].append(line)
        n+=1
    index += 1
sqr[1],sqr[2] = sqr[2],sqr[1]
print(sqr)




for i in range (9):
    line = []
    for x in range(3):
        sqr[]
    