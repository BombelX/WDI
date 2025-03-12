a = int(input("Podaj liczbe: "))
max = [0,0]
len = 100
for i in range(1,a//2+1):
    if a%i == 0:
        b = a/i
        if abs(i-b) < len:
            len = abs(i-b)
            max = [i,b]
print(max)
        