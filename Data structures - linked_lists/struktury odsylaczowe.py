class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def member(zb,elem):
    # prev = None
    while zb != None and elem <zb.val:
        zb = zb.next
    return zb is not None and zb.val == elem

def insert(zb,elem):
    prev = None
    p = zb
    while p is not None and p.val < elem :
        prev = p
        p = zb.next
    if p is not None and p.val == elem:
        return
    new = node(elem)
    if prev != None:
        prev.next = new
        new.next = p
    else:
        new.next = zb
        zb = new
    return zb

# zb = insert(zb,elem)_


def marge_rec(zb1,zb2):
    if zb1 == None:
        return zb2
    if zb2 == None:
        return zb1

    if zb1.val <= zb2.val:
        res = zb1
        res.next = marge_rec(zb1.next,zb2)
    else:
        res = zb2
        res.next = marge_rec(zb1,zb2.next)
    return res

