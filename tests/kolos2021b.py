import math

def is_prime(n):
    if n == 2 or n == 3 or n == 5 or n == 7 : return True
    if n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n == 1: return False
    i = 11
    while i < math.ceil(math.sqrt(n)):
        if n % i == 0:
            return False
        i+=2
        if n % i == 0:
            return False
        i+=4
    #end while
    return True


t1 =[21,34,5654,432,423,43,546,54,3,234,234,234,324,234,23423,432,432,4,256,546,3524,432,432,43,654,654,66,75,756,634,2,342,34,324,45,35,24,5654]
t2 = [43242,432,423,7,32,435,356,466,54,344,234,23,554,664,775,75,634,23,43,645,645,23,432,55,76,86,86,45,345,347,7,565,5,4325,36,356,536,354,4535,34,534]

t1len = len(t1)
t2len = len(t2)
def is_only_2dividers(num):
    for x in range(2,num):
        if num % x == 0:
            if is_prime(x):
                if is_prime(num//x):
                    return True
    return False

def solve(t1,t2):
    t1len = len(t1)
    t2len = len(t2)
    for li in range (1,min(t1len,t2len)):
        sum = 0
        start = 0
        for el in range(0,li):
            sum += t1[el]
        while start+li <= t1len:
            sum -= t1[start]
            start +=1
            sum += t1[start+li]
            sumt2 = 0
            for el in range(0,li):
                sumt2 += t2[el]
            if is_only_2dividers(sum+sumt2):
                return True
            startt2 = 0
            while startt2+li <= t2len:
                sumt2 -= t2[startt2]
                startt2+=1
                sumt2 += t2[startt2+li]
                if is_only_2dividers(sum+sumt2):
                    return True
    return False


            
def run_tests():
    # Test 1: Zestaw z prostymi liczbami
    t1_test1 = [6, 10, 15]  # Suma = 16 (2 * 8), 10, 6, 4 (2 * 2)
    t2_test1 = [4, 9, 5]    # Suma = 14 (2 * 7), 9, 4 (3 * 3)
    assert solve(t1_test1, t2_test1) == True

    # Test 2: Zestaw z liczbami zawierającymi liczby pierwsze
    t1_test2 = [2, 3, 5, 7]  # Suma = 12 (3 * 4), 10, 4, 6 (2 * 3)
    t2_test2 = [5, 11, 13]   # Suma = 24 (2 * 12), 11, 5 (5 * 1)
    assert solve(t1_test2, t2_test2) == True

    # Test 3: Brak możliwości znalezienia odpowiednich kawałków
    t1_test3 = [1, 1, 1]     # Suma = 3 (brak możliwości)
    t2_test3 = [2, 2, 2]     # Suma = 6 (brak możliwości)
    assert solve(t1_test3, t2_test3) == False

    # Test 4: Duża suma elementów
    t1_test4 = [13, 23, 34, 17, 2]  # Suma = 89 (2 * 44.5)
    t2_test4 = [43, 5, 2, 11]       # Suma = 61 (brak możliwości)
    assert solve(t1_test4, t2_test4) == False

    # Test 5: Obie tablice mają tę samą długość i odpowiadające sumy
    t1_test5 = [5, 2, 7, 1]  # Suma = 15 (3 * 5)
    t2_test5 = [3, 2, 5, 1]  # Suma = 11 (brak możliwości)
    assert solve(t1_test5, t2_test5) == True

    # Test 6: Długość kawałków równa 1, oba są liczbami pierwszymi
    t1_test6 = [2]  # Suma = 2 (2 * 1)
    t2_test6 = [3]  # Suma = 3 (brak możliwości)
    assert solve(t1_test6, t2_test6) == True

    # Test 7: Tablice o różnej długości
    t1_test7 = [2, 3, 5]       # Suma = 10 (2 * 5)
    t2_test7 = [11, 12, 13]    # Suma = 36 (brak możliwości)
    assert solve(t1_test7, t2_test7) == False

    # Test 8: Tablice z dużymi liczbami
    t1_test8 = [100003, 100019, 100021]  # Potrzebujemy dużych liczb pierwszych
    t2_test8 = [100003, 99991]            # Potrzebujemy dużych liczb
    assert solve(t1_test8, t2_test8) == False

    print("Wszystkie testy przeszły pomyślnie!")

# Wywołanie funkcji testującej
run_tests()
