def is_l1_contain_in_l2(l1,l2):
    start = l2
    startl2= l1

    while start is not None:

        if start.val == startl2.val:
            cp = startl2    
            potential = start
            while  cp is not None and potential is not None and potential.val == cp.val:
                potential = potential.next
                cp = cp.next
            if cp == None:
                return True
        start = start.next
    return False


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Tworzenie listy l2: 1 -> 2 -> 3 -> 4
l2 = Node(1)
l2.next = Node(2)
l2.next.next = Node(3)
l2.next.next.next = Node(4)

# Tworzenie listy l1: 2 -> 3
l1 = Node(2)
l1.next = Node(3)

# Sprawdzenie, czy l1 zawiera się w l2
print(is_l1_contain_in_l2(l1, l2))  # Powinno zwrócić True
