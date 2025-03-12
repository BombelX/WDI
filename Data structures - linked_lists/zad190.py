def has_odd_fives(num):
    fives_num = 0
    while num > 0:
        if num % 8 == 5:
            fives_num += 1
        num//=8
    return fives_num % 2 ==0
        

def solve(chain):
    prev = None
    head = None
    current = chain
    while current is not None:
        tmp = current.next
        if has_odd_fives(current.val):
            current.next = head
            head = current
            if prev != None:
                prev.next = tmp
        else:
            prev = current
        current = tmp

    return head

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Tworzenie listy 45 -> 25 -> 5 -> 33 -> 7
head = Node(45)
head.next = Node(25)
head.next.next = Node(5)
head.next.next.next = Node(33)
head.next.next.next.next = Node(7)

# Przetwarzanie listy
head = solve(head)

# Wyświetlanie wynikowej listy
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
