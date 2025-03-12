def generate_mask(num):
    num2 = num
    lenght = 0
    cnt = 0
    while  num2 > 0:
        lenght += 1
        num2 //= 10
    for mask in range(1,2**lenght):
        num2 = num
        pot = 1
        bud = 0
        for _ in range(lenght):
            if (mask%2) == 1:
                bud += (num2 % 10) * pot
                pot *= 10
            num2 //= 10
            mask //= 2
        # end 
        if (bud%7) == 0:
            cnt += 1
    return cnt

print(generate_mask(2315))