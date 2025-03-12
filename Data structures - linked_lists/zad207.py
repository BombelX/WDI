class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def solve(chain, s1):
    if chain is None:
        new = Node(s1)
        new.next = new
        return True, new
    
    head = chain
    prev = None
    flag = False
    
    if s1[-1] < chain.val[0]:
        new = Node(s1)
        new.next = chain
        
        last = chain
        while last.next != head:
            last = last.next
        last.next = new
        return True, new

    while chain is not None and s1[-1] > chain.val[0]:
        prev = chain
        chain = chain.next
        if chain == head:
            flag = True
            break

    if not flag and s1[-1] < chain.val[0]:
        new = Node(s1)
        new.next = chain
        prev.next = new
        return True, new
    elif chain.next.val[0] > s1[-1]:
        new = Node(s1)
        new.next = chain.next
        chain.next = new
        return True, new
    else:
        return False, head
def print_list(head):
    if head is None:
        print("Lista jest pusta.")
        return
    result = []
    current = head
    while True:
        result.append(current.val)
        current = current.next
        if current == head:
            break
    print(" -> ".join(result))
# Test 1: Pusta lista
chain = None
result, chain = solve(chain, "ola")
print("Test 1: Dodanie do pustej listy")
print_list(chain)

# Test 2: Lista jednoelementowa
chain = Node("marek")
chain.next = chain
result, chain = solve(chain, "adam")
print("\nTest 2: Dodanie do jednoelementowej listy")
print_list(chain)

# Test 3: Wstawianie na początku
chain = Node("marek")
node2 = Node("zosia")
chain.next = node2
node2.next = chain
result, chain = solve(chain, "adam")
print("\nTest 3: Wstawianie na początku listy")
print_list(chain)

# Test 4: Wstawianie w środku
chain = Node("marek")
node2 = Node("zosia")
chain.next = node2
node2.next = chain
result, chain = solve(chain, "ola")
print("\nTest 4: Wstawianie w środku listy")
print_list(chain)

# Test 5: Wstawianie na końcu
chain = Node("marek")
node2 = Node("ola")
chain.next = node2
node2.next = chain
result, chain = solve(chain, "zosia")
print("\nTest 5: Wstawianie na końcu listy")
print_list(chain)

# Test 6: Lista, gdzie nie można wstawić elementu
chain = Node("marek")
node2 = Node("ola")
chain.next = node2
node2.next = chain
result, chain = solve(chain, "zzz")
print("\nTest 6: Brak możliwości wstawienia elementu")
print_list(chain)
print(f"Result: {result}")
