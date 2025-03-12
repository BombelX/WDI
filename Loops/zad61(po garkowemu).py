
def is_same_elements(a,b):
    '''Funkcja ma na celu sprawdzenie czy 2 liczby składaja sie z tych samych 
    składników (liczy sie liczba wystapień 222 != 22), Przykładem takiej liczby jest 1231 i np 1321'''
    tabA = [0 for _ in range(10)]
    while a > 0:
        tabA[(a%10)] += 1
        a //= 10
    while b != 0:
        tabA[(b%10)] -= 1
        b //= 10
    if max(tabA) == 0 and min(tabA) == 0: 
        # wedlug mnie niemozna tu uzyc sumy bo suma moze byc zero pomimo tego ze liczby niesa rowne
        return True
    return False
        
print(is_same_elements(1234,4321))
