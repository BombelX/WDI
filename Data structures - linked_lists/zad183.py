class node:
    def __init__(self,val):
        self.val = val
        self.next = None

def solve(num_list):
    def revert(list):
        if list is None:
            return list
        prev = None
        while list is not None:
            tmp = list.next
            list.next = prev
            prev = list
            list = tmp
        return prev
    revrs = revert(num_list)
    rev = revrs
    prev = None
    while rev is not None:
        if rev.val+1 < 10:
            rev.val +=1
            break
        else:
            rev.val = 0
            prev = rev
            rev = rev.next

    if rev == None:
        prev.next = node(1)
    return revert(revrs)

# Tworzenie listy reprezentującej liczbę 129
head = node(9)
head.next = node(9)
head.next.next = node(9)

# Zwiększenie liczby o 1
new_head = solve(head)

# Wyświetlanie wynikuSS
current = new_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
