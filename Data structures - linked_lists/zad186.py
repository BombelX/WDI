class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def solve(zb,napis):
    if zb is None :
        zb = Node(napis)
        return True
    if napis < zb.val:
        new = Node(napis)
        new.next = zb
        return  True
    
    while zb is not None and napis < zb.val:
        zb = zb.next
    if zb.val == napis:
        return False
    else:
        tmp = zb.next
        new = Node(napis)
        new.next = tmp
        zb.next = new
        return  True
