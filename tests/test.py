def long_div(num,divider,k):
    print (num//divider, end=",")
    reminder = num%divider
    for _ in range(k):
        print((reminder*10)//divider,end="")
        reminder = (reminder*10)%divider
    
print(long_div(10,3,10))