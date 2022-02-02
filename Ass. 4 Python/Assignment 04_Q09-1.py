import random
def three_heads():
    z = 1
    L = []
    i = 0
    while z==1:
        x = random.randint(0,1)
        if x == 1:
            print("H", end="")
            L.append("H")
        if x == 0:
            print("T", end="")
            L.append("T")
        if i >= 2:
            if L[i-2]=="H" and L[i-1]=="H":
                z=0
                print("\n", "Three heads in a Row!")
        i += 1
three_heads()
            
            
   
