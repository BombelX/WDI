class Node:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.next = None
def print_list(head):
    """Funkcja pomocnicza do wypisywania całej listy."""
    elements = []
    current = head
    while current is not None:
        elements.append((current.a,current.b))
        current = current.next
    print(" -> ".join(map(str, elements)))

res = None
end = False
dl = 0

def fill(start, start_head, head,n):
    global res,end,dl
    print(n)
    if n == dl :
        res = start_head
        end = True
    if end :
        return
    prev = None
    curr = head
    while curr is not None:
        if curr.a == start.b:
            curr_copy = curr
            prev_start = start
            nd = Node(curr.a,curr.b)
            start.next = nd
            start = nd
            if prev is not None:
                prev.next = curr.next
                print_list(start_head)
                fill(start,start_head,head,n+1)
                print_list(start_head)
                print_list(head)

                if not end:
                    prev = curr_copy
                    start = prev_start
                else:
                    return
            else:
                head = curr.next
                print_list(start_head)
                fill(start,start_head,head,n+1)
                print_list(start_head)
                print_list(head)
                if not end:
                    head = curr_copy
                    start = prev_start
                else:
                    return

            
            
        prev = curr
        curr = curr.next
        


def solve_mag_mino(chain):
    if chain is None:
        return None
    global  dl
    head = chain
    start = None

    tmp = chain
    while tmp is not None:
        dl+=1
        tmp = tmp.next

    # Znajdowanie elementu startowego
    while chain is not None:
        curr = head
        flag = True
        while curr is not None:
            if curr.b == chain.a:
                flag = False
                break
            curr = curr.next
        if flag:
            start = chain
            break
        chain = chain.next

    if start is None:
        return None 

    res = None
    end = False
    start_n = Node(start.a,start.b)
    fill(start_n, start_n, head,1)

    return res
# Przykładowa lista klocków domino
head = Node(1, 2)
head.next = Node(2, 3)
head.next.next = Node(3, 4)

result = solve_mag_mino(head)

if res:
    while res:
        print(f"({res.a}, {res.b})", end=" -> ")
        res = res.next
else:
    print("Nie można ułożyć klocków.")
