import math
def find_primes(r1):
    primes = []
    if r1>=2:
        primes.append(2)
    for i in range (3,r1+1,2):
        is_prime = True
        for j in range (2,math.ceil(i/2)):
            if i%j == 0 :
                is_prime = False
        if is_prime :
            primes.append(i)
    
    return primes 
zakres = int(input("do jakiej liczby chcesz znaleźć liczby pierwsze : "))
tab = zakres*[1]
tab[0] = 0

r1  = math.ceil(math.sqrt(zakres))
primes = find_primes(r1)
res = []
for prime in primes:
    actual_num = prime
    while actual_num <= zakres:
        tab[actual_num-1] = 0
        actual_num +=prime
n = 1
for i in tab:
    if i == 1:
        res.append(n)
    n+=1
pierwsze = primes+res

for prime in pierwsze:
    prim = str(prime)
    t = True
    for i in range(len(prim)//2):
        if prim[0] != prim[-1]:
            t = False
            break
    if t:
        for i in range(len(prim)//2):
            prim = prim[1:-1]
            if prim == "":
                continue
            if prim[0] != prim[-1]:
                t = False
                break
            if int(prim) not in pierwsze:
                t = False
    if t:
        print(prime)  
                    
            
            
                
                