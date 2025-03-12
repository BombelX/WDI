def multi(T)

@ca
def check(string)
    n = len(string)
    for i in range(1,1+n//2):
        if n%i == 0:
            for a in range(i):
                for k in range(2,n//i):
                    if string[a] != string[a+k*i]:
                        break
                        

