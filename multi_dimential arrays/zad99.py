T = [
    [7,  1,  5,  9,  3, 11,  8, 13],
    [4,  2, 14, 10,  6, 15,  5,  7],
    [3,  9,  4, 16,  7, 18, 10, 11],  # Ciąg: 3, 6, 9, 12 (zaczyna się w T[2][0], długość 4)
    [5,  6,  5,  8, 14,  2,  3, 16],
    [8,  7,  9, 18, 16,  4, 2,  3],
    [9,  5,  3, 12,  4, 4, 14,  6],  # Ciąg: 2, 4, 8, 16, 32 (zaczyna się w T[1][1], długość 5)
    [7,  6, 11, 15, 8, 20,  7, 12],
    [4,  8,  9,  16, 10,  3, 16,  5]
]

size = len (T[0])
seqs = [[] for _ in range (2*size-1)]
for i in range (size):
    tmp = [0]*(i+1)
    for j in range(0,i+1):
        tmp[j] = T[i-j][j]
    seqs[i] = tmp
for i in range (size-1,0,-1):
    tmp = [0]*(size-i)
    for j in range(i,size):
        tmp[size-j-1] = T[j][size-1-abs(i-j)]
    seqs[size+size-i-1] = tmp
for seq_i in range (2*size-1):
    seq = seqs[seq_i]
    if len(seq) > 3:
        q = seq[1]/seq[0]
        fg = True
        for el in range(1,len(seq)):
            if seq[el]/seq[el-1] != q:
                fg = False
                break
        if fg:
            print(seq)


