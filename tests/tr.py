import math


def trojki(T):
    cnt = 0
    def rek(i,tab,pos):

        rek(i+1,tab+[i],pos+1)
        rek(i+1,tab,pos+1)

        

    for i in range(len(T)):
        rek()

        