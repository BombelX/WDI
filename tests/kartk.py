def convert_to_base(num,base):
    s = "0123456789ABCDEF"
    res = ""
    len_S = 0
    while num > 0:
        res += s[num%base]
        num //= base
        len_S+=1
    res_2 = [""]*len_S
    for i in range(len_S):
        res_2[i] = res[len_S-i-1]
    return res_2,len_S


check_tab = [0]*16
num,len_num = convert_to_base(16,16)


for i in range(len_num):
    inx = int(num[i])

    check_tab[]

print(num)

