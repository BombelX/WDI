number = int(input("Jaką liczbe chcesz podzielic ? "))
f_numbers = []
factor = 2
while number != 1:
    if (number % factor) == 0:
        f_numbers.append(factor)
        number /= factor  
        factor = 2
    else:
        factor +=1
print(f_numbers)