
import math

def is_prime(n):
    if n == 2 or n == 3 or n == 5 :
        return True
    if  n%2 == 0 or n%3 ==0 or n%5 == 0 or n == 1:
        return  False
    i = 5
    while  i < math.ceil(math.sqrt(n)):
        if n%i == 0:
            return False
        i += 2
        if n%i == 0:
            return False
        i +=4
    return  True

def check_mask(mask,t1,t2):
    sum = 0
    flgt1 = flgt2 = False
    i= 0
    while mask > 0:
        trit = mask%3
        match trit:
            case 0:
                sum += t1[i]
                flgt1 = True
            case 1:
                sum += t2[i]
                flgt2 = True
            case 2:
                sum += t1[i] + t2[i]
                flgt1 = flgt2 = True
        mask //= 3
        i+=1
    if flgt1 and flgt2:
        return sum
    else:
        return 0
    
def generete_mask(t1,t2,n):
    max_sum = 0
    for mask in range (1,3**n):
        sum = check_mask(mask,t1,t2)
        if is_prime(sum):
            max_sum = max(sum,max_sum)
    return max_sum



print(generete_mask([1,3,2,4],[9,7,4,8],4))