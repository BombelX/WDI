index = int(input("Podaj ilosc krokow"))
end = False
for num in range(2,10001):
    inx = 0
    str_num = num
    while num != 1:
        num = (num%2)*(3*num+1)+(1-num%2)*num/2
        inx += 1
    if inx == index:
        print(inx,str_num)
        break