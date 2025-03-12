n = 20
tab = [[[] for _ in range(n)] for _ in range(n)]

rows = len(tab[[0][0]])
cols = len(tab[0])
index = 1
print(cols,rows)
mu = 0

while n > 0:

    for up in range(0+mu,cols-mu):
        tab[mu][up] = index
        index+=1
    for rg in range(1+mu,rows-mu):
        tab[rg][rows-mu-1] = index
        index += 1
    for dn in range (rows-mu-1,mu,-1):
        tab[cols-mu-1][dn-1] = index
        index += 1
    for lf in range (rows-mu-1,mu+1,-1):
        tab[lf-1][mu] = index
        index += 1

    mu += 1
    n-=2

for j in range(cols):
    print(tab[j])
