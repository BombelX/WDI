import math 



def find_factors(number):
    sum_of_factors = 0
    for i in range (1,math.ceil(number/2)+1):
        if number%i == 0:
            sum_of_factors += i
    return sum_of_factors


factors = []

for i in range(1,100000):
    factr = [i,find_factors(i)]
    factors.append(factr)
for x in factors:
    for j in factors:
        if j[1] == x[0]:
            if j[0] == x[1] and j[0] != x[0]:
                print(str(x[0]) + " oraz " + str(j[0]) + " to liczby zaprzyjaznione")
