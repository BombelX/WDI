from math import sqrt

t1 = [13,23,43,5,5,3,2,324,54,54,2423,423,432,423,423,432,423,423,43,54,6,467,56,46,3,534,324,234,26,546,355,324,356,545,34,234]
t2 = [344,567,764,34,2,2,1,678,56,456,764,546,43,5345,786,87,745,4,554,787,5,646,56,345,45437,657,5676,654,3,534534534,654,764,765,76]
t1len = len(t1)
t2len=  len(t2)
def check(t1,t2,t1len,t2len):
    for start in range(t1len):
        for li in range(1,24):
            sum = 0
            if start+li <= t1len:
                for endt1 in range(start,start+li):
                    sum += t1[endt1]
                for startt2 in range(t2len):
                    sumt2 = 0
                    if startt2+24-li <= t2len:
                        for x in range(startt2,startt2+(24-li)):
                            sumt2 += t2[x]
                        s = sqrt(sum+sumt2)
                        if s == int(s):
                            return True
    return False

            
# Przykładowe tablice testowe
t1_test1 = [1] * 24  # Tablica z 24 jedynkami (suma zawsze 24)
t2_test1 = [1] * 24  # Tablica z 24 jedynkami (suma zawsze 24)

t1_test2 = [13, 23, 43, 5, 5, 3, 2, 324, 54, 54, 2423, 423, 432, 423, 423, 432, 423, 423, 43, 54, 6, 467, 56, 46]
t2_test2 = [344, 567, 764, 34, 2, 2, 1, 678, 56, 456, 764, 546, 43, 5345, 786, 87, 745, 4, 554, 787, 5, 646, 56, 345]

t1_test3 = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
t2_test3 = [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32]

# Przeprowadzamy testy
print("Test 1:", check(t1_test1, t2_test1, len(t1_test1), len(t2_test1)))  # Oczekiwane False, bo sumy są niskie
print("Test 2:", check(t1_test2, t2_test2, len(t1_test2), len(t2_test2)))  # Różne wartości, oczekiwany wynik zależny
print("Test 3:", check(t1_test3, t2_test3, len(t1_test3), len(t2_test3)))  # Suma powinna być potęgą liczby 2
