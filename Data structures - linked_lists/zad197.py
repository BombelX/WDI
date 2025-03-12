class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def count_elements_in_cycle(chain):

    if chain is None:
        return 0
    rabbit = chain
    turtle = chain
    cycle_pointer = None
    while rabbit is not None and rabbit.next is not None:
        rabbit = rabbit.next.next
        turtle = turtle.next
        if turtle == rabbit:
            cycle_pointer = turtle
            break
    cp = cycle_pointer.next
    cyclen = 1
    while cp != cycle_pointer:
        cp = cp.next
        cyclen  += 1
    return cyclen
    

# Tworzenie listy z cyklem
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node3  # Cykl zaczyna się w node3

# Obliczanie długości cyklu
print(count_elements_in_cycle(head))  # Powinno zwrócić 3
