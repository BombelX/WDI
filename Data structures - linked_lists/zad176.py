class node:
    def __init__(self,val,index):
        self.val = val
        self.index = index
        self.next = None

def initialize_sparse_array(array):
    head = None
    tail = None
    for idx,val in enumerate(array):
        if val != 0:
            new = node(val,idx)
            if head == None:
                head = new
                tail = new
            else:
                tail.next = new
                tail = new
    return head




def set_value(rare,value,index):
    new = node(value,index)
    if rare is None:
        return new
    if index < rare.index:
        new.next = rare
        return new
    curr = rare
    prev = None
    while curr is not None and curr.index < index:
        prev = curr
        curr = curr.next
    if curr is None:
        prev.next = new
        new.next = None
    elif curr.index == index:
        curr.val = value
    else:
        prev.next = new
        new.next = curr
    return rare

def get_value_onId(rare,elem_id):

    while rare is not None and rare.index != elem_id:
        rare = rare.next
    if rare is None:
        return 0
    else:
        return rare.val




# Tworzenie łańcucha
head = node(10, 1)
head.next = node(20, 3)

# Aktualizacja lub wstawianie elementów
head = set_value(head, 5, 0)  # Dodanie na początek
head = set_value(head, 15, 2)  # Dodanie w środku
head = set_value(head, 30, 3)  # Aktualizacja istniejącego elementu
head = set_value(head, 40, 4)  # Dodanie na koniec

# Wyświetlanie łańcucha
current = head
while current is not None:
    print(f"Index: {current.index}, Value: {current.val}")
    current = current.next
