class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve_final(lst):
    if lst is None:
        return None
    head = lst
    last_good_pointer = lst
    current = lst.next  

    while current is not None:
        if current.val < last_good_pointer.val:
            current = current.next  
        else:
            last_good_pointer.next = current  
            last_good_pointer = current  
            current = current.next  

    last_good_pointer.next = None  
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(4)
head.next.next.next.next = Node(3)

# Przetwarzanie listy z poprawioną funkcją
head = solve_final(head)

# Wyświetlanie wynikowej listy
current = head
result = []
while current is not None:
    result.append(current.val)
    current = current.next

print(result)
