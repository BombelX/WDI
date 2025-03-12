import math
tab =  [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2]

tab_len = len(tab)


for lenght in range(3,math.ceil(tab_len//2)):
    tb = [0]*lenght*2
    for x in range(tab_len-lenght*2):
        flg = True
        for i in range(lenght):
            if tab[x+i+lenght]%tab[x+i] != 0:
                flg = False
        if flg:
            print(x,x+lenght-1)


            


