class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



def solve(chain,res1,res2):
    r1,r2 = res1,res2
    cnt = 0
    flag = False
    if chain == None:
        return cnt
    while chain is not None:
        if chain.val >=0 and abs(chain.val)%2 == 0:
            r1.next = chain
            r1 = chain
            r1.next = None
        elif chain.val <=0 and abs(chain.val)%2 == 1:
            r2.next = chain
            r2 = chain
            r2.next = None
        else:
            flag = True
            cnt+=1
        if flag:
            tmp = chain.next
            chain.next = None
            chain =  tmp
        else:
            chain = chain.next
    return cnt


