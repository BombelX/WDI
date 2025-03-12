class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(chain, k):
    if chain is None or k <= 0:
        return chain, 0  

    head = chain
    current = chain
    counts = {}
    removed_count = 0

    while True:
        if current.val not in counts:
            counts[current.val] = [0, []]  
        counts[current.val][0] += 1
        counts[current.val][1].append(current)
        current = current.next
        if current == head:
            break

    for key, (count, nodes) in counts.items():
        if count == k:
            for node in nodes:
                prev = find_previous(head, node)
                if prev is None:
                    temp = head
                    while temp.next != head:
                        temp = temp.next
                    temp.next = head.next
                    head = head.next
                else:
                    prev.next = node.next

                removed_count += 1

    return head, removed_count

def find_previous(head, node):
    """Znajduje poprzedni węzeł w cyklicznej liście"""
    current = head
    while True:
        if current.next == node:
            return current
        current = current.next
        if current == head:
            break
    return None
