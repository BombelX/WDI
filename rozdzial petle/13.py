import math 

def is_perfect(number):
    sum = 1
    rng = int(math.sqrt(number))
    for i in range(2,int(rng)+1):
        if number%i == 0:
            sum += i + number/i
        if number == rng**rng :
            sum -= rng
    if number == sum:
        return True
    else:
        return False

perfect_numbers = []

for i in range(2,1000000,2): # nieznaleziono jeszcze zadnej liczby doskonalej nieparzystej wiec do miliona napewno jej niema(niema dowodu ze niema takiej liczby niema)
    if is_perfect(i):
        perfect_numbers.append(i)
        print(i)

                