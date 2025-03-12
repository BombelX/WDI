


tab = [
[23,343,12,32,54,345,23,44,678],
[98,94,93,88,74,234,333,23,544],
[11,23,44,55,657,676,444,43,90],
[111,234,9959,43,3,94,24,23,49],
]





def solve93(tab):
    rows = 3
    cols = 9
    for row in range(rows):
        flg1 = False
        for col in range(cols):
            num = tab[row][col]
            f2 = True
            while num > 0:
                if (num%10)%2 == 0:
                    break
                num //= 10
            if f2 :
                flg1 = True
                break            
        if not flg1:
            return False
    return True
print(solve93(tab))