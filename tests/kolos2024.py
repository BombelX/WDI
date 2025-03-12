class Node:
    def __init__(self,val):
        self.val = val
        self.next = None




def separate(p):
    dummy1 = Node(0)
    dummy2 = Node(0)
    head1= dummy1
    head2 = dummy2
    p = p.next
    head = p
    prev = None
    while p != head:
        if p.val%2==0 and p.val>0:
            dummy1.next = p
            dummy1 = p
            prev = p
        elif p.val%2==1 and p.val<0:
            dummy2.next = p
            dummy2 = p
            prev = p
        else:
            prev.next = p.next
            
        p = p.next
    dummy1.next = head1.next
    dummy2.next = head2.next
    return head1.next,head2.next
        
        


