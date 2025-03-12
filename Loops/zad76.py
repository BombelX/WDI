from math import sqrt

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i < sqrt(n+1) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True

def sum_mask(t1,t2,mask):
    usedt1 = usedt2 = False
    sum = 0
    
    for i in range(len(t1)):
        if mask % 3 == 0:
            usedt1 = True
            sum += t1[i]
        elif mask % 3 == 1:
            usedt2 = True
            sum+= t2[i]
        else:
            usedt1 = usedt2 = True
            sum += t1[i] + t2[i]        
        mask //= 3
    if usedt1 == True and usedt2 == True:  #sprawdzamy czy został uzyty min 1 element z kazdej z tablic
        return sum
    else:
        return -1
    
def base3_mask(t1,t2):
    cnt = 0
    # generujemy maski w systemie 3  0 - bierzemy element o jakims indexie 
    # tylko z t1, 1 -tylko element z t2, 2 element z t1 i t2
    for mask in range(3 ** len(t1)):
        sum = sum_mask(t1,t2,mask)
        if  sum != -1 and is_prime(sum):
            cnt+=1
    return cnt
            
        

t1 = [6, 765, 76, 53, 242, 432, 342, 465, 5, 34]
t2 = [2342, 3453, 65654, 43, 2, 12, 3, 453, 6, 78]
print(base3_mask(t1, t2))
