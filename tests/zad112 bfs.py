tab = [
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
     ]
tab_size = len(tab)

queue = [0]*tab_size*1000000
actual_end_index = 0
front = 0

for i in range(tab_size):
    if tab[0][i] == 0:
        queue[actual_end_index] = [0,i,0] # x , y ,glebokosc
        actual_end_index += 1

# def pop_elem(pop_index,end,queue):
    # for i in range(pop_index+1,end):
    #     queue[i-1] = queue[i]
    # queue[end] = 0
    # return queue,end-1




while actual_end_index > 0:
    pos  = queue[front]
    if pos[0] >= 0 and pos[0] <tab_size and pos[1]>=0 and pos[1] <tab_size:
        if tab[pos[0]][pos[1]] == 0:
            if pos[0] == tab_size-1:
                print (pos[2])
                break
        queue[actual_end_index] = [pos[0]+2,pos[1]+1,pos[2]+1]
        actual_end_index+=1
        queue[actual_end_index] = [pos[0]+2,pos[1]-1,pos[2]+1]
        actual_end_index+=1
        queue[actual_end_index] = [pos[0]+1,pos[1]+2,pos[2]+1]
        actual_end_index+=1
        queue[actual_end_index] = [pos[0]+1,pos[1]-2,pos[2]+1]
        actual_end_index+=1

    # queue,actual_end_index = pop_elem(0,actual_end_index,queue)
    front += 1
    