

def approx_e(size):
    e = [0 for _ in range(size)]
    a = [0 for _ in range(size)]
    
    e[0] = 1
    a[0] = 1
    n,b,p = 1,True,0
    while b:
        b = False
        p = 0
        for i in range (size-1,-1,-1):
            s= e[i] + a[i] + p
            e[i] = s%10
            p = s//10
        #end for
        n+=1
        r = 0 
        for i in range (size):
            t = (r*10+a[i])
            a[i] = t//n
            r = t%n
            if a[i] > 0:
                b = True
            #end if
        #end for
    #end while

    print (str(e))
#end func
approx_e(10000)