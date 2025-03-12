class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(num_1, num_2):
    def revert(lst):
        prev = None
        while lst is not None:
            next_node = lst.next
            lst.next = prev
            prev = lst
            lst = next_node
        return prev

    # Odwracamy listy wejściowe
    num1_rev = revert(num_1)
    num2_rev = revert(num_2)

    carry = 0
    new_head = None
    tail = None

    # Dodajemy liczby reprezentowane przez listy
    while num1_rev is not None or num2_rev is not None or carry > 0:
        val1 = num1_rev.val if num1_rev is not None else 0
        val2 = num2_rev.val if num2_rev is not None else 0

        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        new_node = Node(new_val)
        if new_head is None:
            new_head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

        # Przechodzimy do kolejnych węzłów
        if num1_rev is not None:
            num1_rev = num1_rev.next
        if num2_rev is not None:
            num2_rev = num2_rev.next

    # Przywracamy oryginalną kolejność listy wynikowej
    return revert(new_head)

    # Liczba 342 (3 -> 4 -> 2)
num1 = Node(3)
num1.next = Node(4)
num1.next.next = Node(2)

# Liczba 465 (4 -> 6 -> 5)
num2 = Node(4)
num2.next = Node(6)
num2.next.next = Node(5)

# Dodanie liczb
result = solve(num1, num2)

# Wyświetlanie wyniku
current = result
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
