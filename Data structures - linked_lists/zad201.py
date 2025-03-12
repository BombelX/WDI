def marge_two_sorted(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.val> l2.val:
        head = l2
        l2 = l2.next
    else:
        head = l1
        l1 = l1.next

    
    current = head

    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
        
    if l1 is not None:
        current.next = l1
    else:
        current.next = l2

    return head


        
def merge_two_sorted_in_place(l1, l2):
    # Ustal głowę wynikowej listy
    if l1.val > l2.val:
        l1, l2 = l2, l1  # Zamień l1 i l2, jeśli l2 ma mniejszą wartość
    head = l1  # Ustaw głowę listy na mniejszy węzeł

    # Scalanie w miejscu
    while l1 is not None and l2 is not None:
        if l1.next is None or l1.next.val > l2.val:
            temp = l2.next
            l2.next = l1.next
            l1.next = l2
            l2 = temp
        l1 = l1.next

    return head

