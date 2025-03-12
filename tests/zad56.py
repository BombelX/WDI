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


def different_digits(n):
    tab = [False for _ in range(10)]
    while n > 0 :
        reminder = n%10
        if tab[reminder]:
            return False
        else:
            tab[reminder] = True
        n //= 10
    return True

def cutter(k):
    max_k = 0
    num_len = math.ceil(math.log10(k))
    for left_cut in range(num_len):
        for right_cut in range(num_len-left_cut):
            tmp_k = k
            tmp_k = tmp_k%(10**(num_len-left_cut))
            tmp_k = tmp_k//(10**right_cut)
            if is_prime(tmp_k) and different_digits(tmp_k) :
                max_k = max(max_k,tmp_k)
    return max_k
print(cutter(1202742516))