max = [0,0]
for num in range(2,10001):
    inx = 0
    str_num = num
    while num != 1:
        num = (num%2)*(3*num+1)+(1-num%2)*num/2
        inx += 1
    if inx > max[0]:
        max = [inx,str_num]
print(max)