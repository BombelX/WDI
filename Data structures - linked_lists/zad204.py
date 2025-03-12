# def find_min(chain):
#     if chain is None:
#         return [None, None]

#     prev_mini = None
#     mini = chain
#     prev = None
#     current = chain
#     while current is not None:
#         if current.val < mini.val:
#             mini = current
#             prev_mini = prev
#         prev = current
#         current = current.next
#     if prev_mini is not None:
#         prev_mini.next = mini.next
#     else:
#         chain = mini.next

#     return [mini, chain]


# def solve(l1,l2):
#     new = None
#     mini = [None,None]
#     while l1 is not None and mini[1] is not None:
#         if mini[0] == None:
#             mini = find_min(l2)
#         if new == None:
#             if mini.val < l1.val:
#                 new = mini[0]
#                 mini = find_min(l2)
#             else:
#                 new = l1
#                 l1 = l1.next

#         else:
#             if mini[0].val < l1.val:
#                 new.next = mini[0]
#                 new = mini[0]
#             elif l1 is not None:
#                 new.next = l1
#                 new = l1
#                 l1 = l1.next
#     if l2 is None:
#         new.next = l1
#     else:
#         mini = find_min(l2)
#         while mini[0] is not None:
#             new.next = mini[0]
#             new = mini[0]
#             mini = find_min(l2)
#     return new
        

def find_min(chain):
    if chain is None:
        return [None, None]
    prev_mini = None
    mini = None
    prev = None
    head = chain  # Zachowujemy wskaźnik na początek listy

    while chain is not None:
        if mini is not None:
            if mini.val > chain.val:
                mini = chain
                prev_mini = prev
        else:
            mini = chain
        prev = chain
        chain = chain.next

    # Usuwanie najmniejszego elementu
    if prev_mini is not None:
        prev_mini.next = mini.next
    else:
        head = mini.next  # Jeśli najmniejszy element jest na początku

    return [mini, head]


def solve(l1, l2):
    new = None  # Głowa nowej listy
    tail = None  # Ogon nowej listy
    mini = [None, l2]

    while l1 is not None or mini[1] is not None:
        if mini[0] is None and mini[1] is not None:
            mini = find_min(mini[1])

        if new is None:  # Inicjalizacja głowy nowej listy
            if mini[0] is not None and (l1 is None or mini[0].val < l1.val):
                new = mini[0]
                tail = new
                mini = find_min(mini[1])
            else:
                new = l1
                tail = new
                l1 = l1.next
        else:  # Dodawanie kolejnych elementów do listy
            if mini[0] is not None and (l1 is None or mini[0].val < l1.val):
                tail.next = mini[0]
                tail = mini[0]
                mini = find_min(mini[1])
            else:
                tail.next = l1
                tail = l1
                l1 = l1.next

    return new


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Przykład użycia
# Lista 1: 2 -> 3 -> 5 -> 7 -> 11
l1 = Node(2)
l1.next = Node(3)
l1.next.next = Node(5)
l1.next.next.next = Node(7)
l1.next.next.next.next = Node(11)

# Lista 2: 8 -> 2 -> 7 -> 4
l2 = Node(8)
l2.next = Node(2)
l2.next.next = Node(7)
l2.next.next.next = Node(4)

# Rozwiązanie
result = solve(l1, l2)

# Drukowanie wyniku
print("Lista wynikowa:")
print_list(result)