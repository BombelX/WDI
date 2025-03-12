class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
def has_cycle(chain):
    if chain is None:
        return False
    rabbit = chain
    turtle = chain
    while rabbit is not None and rabbit.next is not None:
        turtle = turtle.next
        rabbit = rabbit.next.next

        if turtle == rabbit:
            break
    start = chain
    while start != turtle:
        turtle = turtle.next
        start = start.next
    return start