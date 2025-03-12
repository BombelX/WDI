
import time

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def print_list(head):
    """Funkcja pomocnicza do wypisywania całej listy."""
    elements = []
    current = head
    while current is not None:
        elements.append(current.val)
        current = current.next
    print(" -> ".join(map(str, elements)))


def insert(num,chain):
    if chain is None:
        return Node(num)
    head = chain
    prev = None
    while chain is not None:
        prev = chain
        chain = chain.next
        nm = chain.val
        if abs(num) < abs(nm):
            new = Node(num)
            new.next = chain
            if prev is not None:
                prev.next = new
                return head
            else:
                head = chain
                return head
    prev.next = Node(new)
            
            
def repair(p):
    head = p
    while True:
        current = head
        prev = None
        flag = True
        while current is not None:
            if current.next is not None:
                q = current.next.val/current.val
                if prev is not None and abs(prev.val*q - current.val)>1:
                    flag = False
                    insert(prev.val*q,head)
                    print("Po naprawie kroku:")
                    time.sleep(1)
                    print_list(head)
                    break
                else:
                    prev = current
                    current = current.next
            else:
                break
        if flag:
            return head      
def create_list(values):

    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head
print("Przykład 1:")
head = create_list([1.5, 1.8, 2.59, 3.11, 3.73, 4.48, 5.37, 6.45, 7.74])
print("Początkowa lista:")
print_list(head)
head = repair(head)
print("Końcowa lista:")
print_list(head)