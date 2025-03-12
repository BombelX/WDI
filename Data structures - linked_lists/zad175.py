class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def exist_in_chain(zb,elem):
    if zb is None:
        return False
    while zb.next is not None:
        if zb.val == elem:
            return True
        zb = zb.next
    return False

# zakladamy ze 
def insert_to_chain(zb,elem):
    new = node(elem)
    if zb is None:
        return new
    if elem < zb.val:
        new.next = zb
        return new
    prev = None
    curr = zb
    while curr is not None and curr.val < elem:
        prev = curr
        curr = curr.next
    prev.next = new
    new.next = curr

    return zb
def remove_from_chain(zb,elem):
    if zb is None:
        return zb
    if elem == zb.val:
        return zb.next
    prev = None
    curr = zb
    while curr is not None and curr.val != elem:
        prev = curr
        curr = curr.next
    if curr is not None:
        prev.next = curr.next
    return zb

    


head = node(1)
head.next = node(3)
head.next.next = node(5)

# Wstawianie elementów
head = insert_to_chain(head, 0)  # Wstawianie na początek
head = insert_to_chain(head, 4)  # Wstawianie w środek
head = insert_to_chain(head, 6)  # Wstawianie na koniec

# Wyświetlanie łańcucha
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next

