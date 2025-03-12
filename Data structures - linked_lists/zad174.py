class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_chain(chain):
    if chain is None:
        return 0
    cnt = 1
    while chain.next is not None:
        chain = chain.next
        cnt += 1
    return cnt 
