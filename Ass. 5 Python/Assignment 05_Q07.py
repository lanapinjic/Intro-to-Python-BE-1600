L = [[0,0,0],
     [0,0,0],
     [0,0,0],
     [0,0,0]]
#part a
print("part a")

for b in range(len(L)):
    
    for c in range(len(L[b])):
        
        print(L[b][c], end= "") 
    print()
    
#part b  
print("part b")

for b in range(len(L)):
    for c in range(len(L[b])):
        n = 0
        
        for i in range(3):
            
            L[0][n] = 1
            n += 1
        n = 0
        
        for i in range(3):
            
            L[1][n] = 3
            n+= 1
        n = 0
        
        for i in range(3):
            
            L[2][n] = 3
            n += 1
        n = 0
        
        for i in range(3):
            
            L[3][n] = 3
            n += 1
            
        print(L[r][c], end= "")
    print()

#part c
print("part c")

for b in range(len(L)):
    
    for c in range(len(L[b])):
        
        n = 0
        for i in range(4):
            
            L[n][0] = 2
            n += 1
        n = 0
        for i in range(4):
            
            L[n][1] = 2 * L[0][0]
            n += 1
        n = 0
        for i in range(4):
            
            L[n][2] = 2 * L[1][1]
            
            n += 1
            
        print(L[b][c], end = "")
    print()



