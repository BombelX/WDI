class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
def is_good(num):
    one = 0
    while num > 0:
        one += num%2
        num //= 2
    return one%2 == 1
def solve(chain):
    current  = chain
    while current is not None:
        next_node = current.next
        if is_good(current.val):
            if current.prev is not None:
                current.prev.next = current.next
            else:
                chain = current.next
            if current.next is not None:
                current.next.prev = current.prev
        current = next_node
    return chain

# Tworzenie listy 5 <-> 7 <-> 8 <-> 15 <-> 6
head = Node(5)
node2 = Node(7)
node3 = Node(8)
node4 = Node(15)
node5 = Node(6)

# Łączenie w listę dwukierunkową
head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev = node4

# Przetwarzanie listy
head = solve(head)

# Wyświetlanie wynikowej listy
current = head
result = []
while current is not None:
    result.append(current.val)
    current = current.next

print(result)

