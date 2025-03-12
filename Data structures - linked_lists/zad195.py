class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def remove_longest__growing_subchain(chain):
    head = chain
    longest = 0
    longest_start = chain
    longest_end = None
    tmp = 0
    tmp_start = chain
    prev = None
    while chain is not None :
        if prev == None:
            tmp =1
        elif prev.val < chain.val:
            tmp +=1
        else:
            if tmp > longest:
                longest = tmp
                longest_start = tmp_start
                longest_end = chain
            tmp_start = chain
            tmp = 1
        prev = chain
        chain = chain.next
    if tmp > longest:
        longest = tmp
        longest_start = tmp_start
        longest_end = chain
    if longest_start == chain:
        return longest_end
    else:
        if longest_end is not None:
            longest_start.next = longest_end
        else:
            longest_start.next = None
    return head
    

# Tworzenie listy 1 -> 2 -> 3 -> 1 -> 4 -> 5 -> 6 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(1)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next.next = Node(3)

# Usuwanie najdłuższego rosnącego podciągu
head = remove_longest__growing_subchain(head)

# Wyświetlanie wynikowej listy
current = head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
