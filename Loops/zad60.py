def convert_base(num,base = 10):
    res = ""
    while num > 0:
        reminder = num % base
        num //= base
        res = str(reminder) + res
    return res
print(convert_base(7,2))        
    