from math import sqrt,ceil

def eratosthenes_sieve(limit):
    sieve = [True for _ in range(limit)]
    sieve[0] = sieve[1] = False
    for i in range (2,ceil(sqrt(limit))):
        for j in range (i*i,limit,i*i):
            sieve[j] = False
    for i in range(1,len(sieve)):
        if sieve[i]:
            print(f"{i} ", end="")
eratosthenes_sieve(25)        