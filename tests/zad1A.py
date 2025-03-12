from math import sqrt,ceil
def f_primes(N):
    cnt = 0
    sieve = [True for _ in range(N)]
    sieve[0] = sieve[1] = False
    for i in range(2,ceil(sqrt(N))):
        for j in range(i*i,N,i):
            sieve[j] = False
            cnt += 1
    return sieve


tab = [i for i in range (2,46)]
sieve = f_primes(1000)

def prime_div(i):
    t = []
    for j in range(1,i+1):
        if sieve[j]:
            if i%j == 0:
                t.append(j)
    return(t)
    
res = []
xxx = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45]
inx = 0
for i in range(0,len(xxx)):
    t = prime_div(xxx[i])
    for j in range(i-2,i+2+1):
        if j != i and j>0 and j < len(xxx):
            if t == prime_div(xxx[j]):
                if xxx[j] not in res:
                    res.append(xxx[j])
                if xxx[i] not in res:
                    res.append(xxx[i])
                break
print(res)
    

