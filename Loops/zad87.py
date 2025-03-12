import math 
def is_prime(n):
    if n == 2 or n == 3 or n == 5: return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0: return False
    i = 5
    while i < math.ceil(math.sqrt(n)):
        if n%i == 0:
            return False
        i +=2
        if n%i == 0:
            return False
        i += 4
    return True



def tw_dziekana():
    if n == 2 or n ==3 or n == 5: return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0 : return False
    i = 5
    while i < math.ceil(math.sqrt(n)):
        if n%i == 0:
            return False
        i+=2
        if n%i == 0:
            return False
        i+=4
    return True
max_c = 0

tab = [1,13,44,52,234,2345,23435,234565,234955]
n = len(tab)
ilo = 1
for x in range(n):
    if x == ilo :
        max_c = max(max_c,x)
    if is_prime(x):
        ilo *= x
print(max_c)
    