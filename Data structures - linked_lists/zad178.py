

def revert(list):
    # if list is None:
    #     return list
    prev = None
    while list is not None:
        tmp = list.next
        list.next = prev
        prev = list
        list = tmp
    return prev

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Funkcja pomocnicza do wyświetlania listy
def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Tworzenie listy
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


print("Oryginalna lista:")
print_list(head)

# Odwracanie listy
head = revert(head)

print("Odwrócona lista:")
print_list(head)
