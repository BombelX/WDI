class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert(zb, elem):
    prev = None
    p = zb
    while p is not None and p.val < elem:
        prev = p
        p = p.next

    if p is not None and p.val == elem:
        return zb  

    new_node = Node(elem)
    if prev is not None:
        prev.next = new_node
        new_node.next = p
    else:
        new_node.next = zb
        zb = new_node

    return zb


def repair(chain):
    cnt = 0
    head = chain
    while True:
        current = head
        prev2 = None
        prev = None
        modified = False  
        while current is not None:
            if prev2 and prev is not None:
                q = current.val / prev.val
                expected = prev2.val * q
                if expected != prev.val and not exists_in_list(head, int(expected)):
                    head = insert(head, int(expected))
                    cnt += 1
                    modified = True
                    break
            prev2 = prev
            prev = current
            current = current.next

        if not modified:  
            break

    return cnt


def exists_in_list(head, value):
    """Sprawdza, czy wartość istnieje w liście"""
    current = head
    while current is not None:
        if current.val == value:
            return True
        current = current.next
    return False


head = Node(4)
head.next = Node(-32)
head.next.next = Node(-128)
head.next.next.next = Node(-2048)

added = repair(head)

current = head
while current:
    print(current.val, end=" → " if current.next else "\n")
    current = current.next

print(f"Liczba dodanych elementów: {added}")