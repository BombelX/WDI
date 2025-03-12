
import math

def generate_fibb(n):
    tab = [0]*n
    a,b = 1,1
    fibb = 0 
    inx = 0
    while fibb <= n:
        a,b = fibb,a
        fibb = a+b
        tab[inx] = fibb
        inx += 1
    return [elem for elem in tab[:tab.index(0)-1]]
        
tab = [3, 3, 8, 9, 2, 12, 3, 5, 14, 7, 11, 13, 17, 15, 19, 23, 29, 31, 37, 41, 43, 16, 47, 53, 59, 61, 67, 71, 73, 79, 
83, 89, 97, 101, 10, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 
197, 199, 18, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 20, 409, 419, 421, 431, 433, 439, 443, 
449, 457, 461]

size = 100

fibb = generate_fibb(size)
flag = True

def is_prime(number):
    for i in range(2,math.ceil(math.sqrt(number))+1):
        if number%i == 0 :
            return False
    return True
def is_composite(num):
    cnt = 0
    for i in range(1,num+1):
        if num%i == 0:
            cnt += 1
            if cnt > 2:
                return True
    return False
    
for num in fibb:
    if not is_composite(tab[num]):
        flag = False
        break
if flag:
    for i in range(0,size+1):
        if i in fibb:
            continue
        else:
            if is_prime(tab[i]):
                break
            elif i == size:
                flag = False
                
                
        
if flag:
    print("sukces")
else:
    print("zle")
        
        
    