from math import sqrt,ceil,log10
def is_palindrom(n):
    dl = ceil(log10(n))

    while dl > 1:
        l = n // 10**(dl-1)
        p = n % 10
        n = n% 10**(dl-1)
        n = n//10
        if p != l:
            return False
        dl -=2

    return  True
print(is_palindrom(19283))

def base_convert(n,base):
    multip = 1
    res = 0
    while n > 0 :
        res += (n%base)*multip
        n //= base
        multip *= 10
    return res

print(base_convert(13,4))