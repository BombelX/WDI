import math

x = math.sqrt(0.5)
for i in range(50):
    x = math.sqrt(0.5+0.5*x)
    print(x)
    
#niewiem jak to dziala