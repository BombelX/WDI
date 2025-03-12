
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbe: "))
c = int(input("Podaj trzecią liczbę: "))

def find_first_factors(number):
    f_numbers = []
    factor = 2
    while number != 1:
        if (number % factor) == 0:
            f_numbers.append(factor)
            number /= factor  
            factor = 2
        else:
            factor +=1
    return(f_numbers)
def NWW(a,b):
    a = find_first_factors(a)
    b = find_first_factors(b)
    tmp = []
    for elem in a:
        if elem not in b:
            tmp.append(elem)
    tmp = tmp+b
    res = 1
    for num in tmp:
        res *= num
    return(res)

print(NWW(NWW(a,b),c))
