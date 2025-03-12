class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve185(list,key):
    if list is None:
        return  Node(key) 
    head = list
    prev = None

    while list is not None and list.val != key:
        prev = list
        list = list.next
    if list.val == key:
        prev.next = list.next
    else:
        list.next = Node(key)
    return head