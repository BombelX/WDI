class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_min(chain,more_then):
    mi_n = chain
    while chain is not None:
        if mi_n.val[0] > chain.val[0] and chain.val[0] > more_then:
            mi_n = chain
        
    if mi_n.val > more_then:
        return mi_n
    else:
        return None



def solve(chain):
    current = chain
    min = find_min(chain,0)
    tmp = 0
    while is_next(chain) != None:
        prev.next = nex_ta 