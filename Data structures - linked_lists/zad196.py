class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def has_cycle(chain):
    if chain is None:
        return False
    rabbit = chain
    turtle = chain
    while rabbit is not None and rabbit.next is not None:
        turtle = turtle.next
        rabbit = rabbit.next.next

        if turtle == rabbit:
            return True
    return False

# Tworzenie listy z cyklem
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  # Cykl zaczyna się w node2

# Sprawdzenie cyklu
print(has_cycle(head))  # Powinno zwrócić True

# Tworzenie listy bez cyklu
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)

# Sprawdzenie cyklu
print(has_cycle(head2))  # Powinno zwrócić False
