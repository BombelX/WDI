n = int(input("Podaj makszymalna dlugos przeciewprostakatnej"))

a,b,c = 1,1,1

for a in range(1,n-2):
    for b in range(1,n-1):
        for c in range (1,n):
            if (pow(a,2) + pow(b,2)) == pow(c,2):
                if a < b and b < c :
                    print(a,b,c)
        
        