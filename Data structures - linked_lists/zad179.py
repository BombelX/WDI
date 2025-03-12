class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(chain):
    h0,h1,h2,h3,h4,h5,h6,h7,h8,h9= None,None,None,None,None,None,None,None,None,None
    s0,s1,s2,s3,s4,s5,s6,s7,s8,s9= None,None,None,None,None,None,None,None,None,None

    if chain is None:
        return None
    else:
        while chain is not None:
            last = chain.val%10
            if exec(f"h{last} == None"):
                exec(f"h{last} = {node(chain.val)}")
                exec(f"s{last} = h{last}")
            else :
                exec(f"h{last}.next = node(chain.val)")
                exec(f"h{last} = h0.next")

            chain = chain.next
    for i in range(9):
        exec(f"h{i}.next = s{i+1}")
    return s0