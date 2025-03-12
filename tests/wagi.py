odw = [1,3,5,7,10,24]

# def waga(t,n,p=0):
#     if n==0: return True
#     if p==len(t): return False
#     return waga(t,n-t[p],p+1) or waga(t,n,p+1) or waga(t,n+t[p],p+1)
# print(waga(odw,2))
    
def waga(t,n,p=0,res=[]):
    if n == 0:
        print(res)
        return
    if p == len(t):
        return
    waga(t,n-t[p],p+1,res+[t[p]])
    waga(t,n,p+1,res)
    waga(t,n+t[p],p+1,res+[-t[p]])


waga(odw,35)