from collections import Counter

def is_same_elements(a,b):
    '''Funkcja ma na celu sprawdzenie czy 2 liczby składaja sie z tych samych 
    składników (liczy sie liczba wystapień 222 != 22), Przykładem takiej liczby jest 1231 i np 1321'''
    a,b = str(a),str(b)
    if Counter(a) == Counter(b):
        return True
    else:
        return False
print(is_same_elements(1234,4321))