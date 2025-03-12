# zakladamy ze lista jest posortowana 

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(chain):
    last_unique =  chain
    if chain is not None :
        current = chain.next
    else :
        return None
    while current is not None:
        if current.val != last_unique.val:
            last_unique.next = current
            last_unique = current
        current = current.next
    if last_unique is not None :
        last_unique.next = None
    return chain
# Tworzenie listy 1 -> 1 -> 2 -> 3 -> 3 -> 4
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(4)

# Przetwarzanie listy
head = solve(head)

# Wyświetlanie wynikowej listy
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
