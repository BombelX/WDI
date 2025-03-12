#Zadanie 27.
# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie,
# czy liczba naturalna jest palindromem, a następnie
# czy jest palindromem w systemie dwójkowym.

a = input("Podaj liczbe ktora chcesz sprawdzić : ")

def is_palindrom(a):
    flag = True
    for i in range(len(a)//2):
        if a[i] != a[-1]:
            flag = False
            break
    return flag        

if is_palindrom(a):
    print("Tak jest to palindrom")
else:
    print("Niejest to palindrom")

if is_palindrom(str(bin(int(a)))):
    print("Tak jest to palindrom binarny")
else:
    print("Niejest to palindrom binarny")