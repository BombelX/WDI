def next_permutation(perm):
    # Step 1: Find the largest index i such that perm[i] < perm[i + 1]
    i = len(perm) - 2
    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    # Step 2: If such an i exists, find the largest index j such that perm[j] > perm[i]
    if i >= 0:
        j = len(perm) - 1
        while perm[j] <= perm[i]:
            j -= 1
        
        # Step 3: Swap perm[i] and perm[j]
        perm[i], perm[j] = perm[j], perm[i]

    # Step 4: Reverse the sublist from i+1 to the end
    perm[i + 1:] = reversed(perm[i + 1:])

def all_permutations(n):
    # Start with the first permutation [1, 2, ..., n]
    perm = list(range(1, n + 1))
    
    # Print the first permutation
    print(perm)
    
    while True:
        next_permutation(perm)
        if perm == sorted(perm, reverse=True):
            # If the permutation is in descending order, we've reached the last one
            break
        print(perm)

# Example usage for n = 4
all_permutations(4)
