def print_tree(p):
    if p is not None:
        print(p.val)
        print_tree(p.left)
        print_tree(p.right)

def czy_nal(p,val):
    if p is None:
        return False
    if p.val == val:
        return True
# metoda leniwego ojca xd

def rozmiar(proot):
    if proot == None:
        return 0
    return rozmiar(proot.right) + rozmiar(proot.left) +1


def liscie_cnt(proot):
    if proot == None:
        return 0
    if proot.left == None and proot.right == None:
        return 1
    return rozmiar(proot.right) + rozmiar(proot.left)

def zlicz(proot,n):
    if proot == None:
        return 0
    if n==0:
        return 1
    return zlicz(proot.left,n-1)+zlicz(proot.right,n-1)
def zlicz_pot(proot):
    if proot == None:
        return 0
    
print(False|False)