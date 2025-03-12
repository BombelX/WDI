def is_good(num):
    one = 0
    two = 0
    while num != 0:
        if num % 3 == 1:
            one += 1
        elif num % 3 == 2:
            two += 1
        num //= 3
    return two < one
        

def solve(chain):
    current = chain
    lastgood = None
    head = None

    while current is not None :
        if is_good(current.val):
            if lastgood is None:                 
                head = current
                lastgood = current
            else:
                lastgood.next = current
                lastgood = current
        current = current.next
    if lastgood is not None:
        lastgood.next = None
    return head
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Tworzenie listy 10 -> 20 -> 5 -> 25 -> 7
head = Node(10)
head.next = Node(20)
head.next.next = Node(5)
head.next.next.next = Node(25)
head.next.next.next.next = Node(7)

# Przetwarzanie listy
head = solve(head)

# Wyświetlanie wynikowej listy
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
