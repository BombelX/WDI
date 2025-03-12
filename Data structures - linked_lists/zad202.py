class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def cnt_how(li1,li2):
    cnt = 0
    while li1 is not None:
        l2_head = li2
        prev = None
        while l2_head is not None:
            if l2_head.val == li1.val:
                cnt += 1
                if  prev is not None:
                    prev.next = l2_head.next
                else:
                    li2 = l2_head.next
                break
            prev = l2_head
            l2_head = l2_head.next
        
        li1 = li1.next
    return cnt,li2

# dziala

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Funkcja do drukowania listy
def print_list(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Przykładowe listy
li1 = Node(1)
li1.next = Node(3)
li1.next.next = Node(5)

li2 = Node(3)
li2.next = Node(4)
li2.next.next = Node(5)
li2.next.next.next = Node(6)

# Wywołanie funkcji
removed_count, updated_li2 = cnt_how(li1, li2)

# Wynik
print("Liczba usuniętych elementów:", removed_count)
print("Zaktualizowana lista li2:")
print_list(updated_li2)
