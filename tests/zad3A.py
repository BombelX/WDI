tab = [7,8,6,4,7,3]
max_c = 0
n = len(tab)

def is_prime(n):
    if n == 2 or n == 3 or n == 5:
        return True
    if n == 1 or n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False
    i = 5
    while i < n:
        if n%i == 0:
            return False
        i+=2
        if n%i == 0:
            return False
        i+=4
    return True



for start in range(n):
    for end in range(start+1,n+1):
        tabA = tab[start:end]
        flg = True
        sum = tabA[0]
        ilo = tabA[0]
        for i in range(1,end-start):
            if flg:
                sum += tabA[i] 
                ilo *= tabA[i]
                flg = False
            else:
                sum *= tabA[i]
                ilo += tabA[i]
                flg = True
        ln = end-start
        if is_prime(ilo):
            max_c = max(ilo,max_c)
        if is_prime(sum):
            max_c = max(sum,max_c)
            
            
print(max_c)

