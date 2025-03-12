class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(polynomial_1,polynomial_2):
    head = None
    current = None
    while polynomial_1 is not None or polynomial_2 is not None:
        
        new_value = 0
        if polynomial_1 is not  None:
            new_value += polynomial_1.val
            polynomial_1 = polynomial_1.next
        if polynomial_2 is not None:
             new_value -= polynomial_2.val
             polynomial_2 = polynomial_2.next
        if current is None:
            current = Node(new_value)
            head = current
        else:
            new = Node(new_value)
            current.next = new
            current = new
        
    return head