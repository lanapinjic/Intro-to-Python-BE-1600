X = []

#getdata function

def getData(L):
    
    print("Enter highest temperatures for each month of the year")
    
    for i in range(2):
        
        temp = []
        
        for j in range(12):
            
            print("Month", j+1, ":", end ="")
            
            x = int(input())
            
            temp.append(x)
            
        X.append(temp)
        
        print("Enter lowest temperatures for each month of the year")
        
    return X

#average high function
def averageHigh():
    
    for i in range(len(X)):
        
        acc = 0
        
        for j in range(len(X[i])):
            
            acc = acc + X[0][j]
            
        avg = acc / 12
        
    return avg


#average low function
def averageLow():
    for i in range(len(X)):
        
        acc = 0
        
        for j in range(len(X[i])):
            
            acc = acc + X[1][j]
            
        avg = acc / 12
        
    return avg

#hightemp function
def highTemp():
    
    X2 = []
    
    for i in range(len(X)):
        
        for j in range(len(X[i])):
            
            X2.append(X[0][j])
            
            highesttemp = max(X2)
            
    return highesttemp

#low temp function
def lowTemp():
    
    X2 = []
    
    for i in range(len(X)):
        
        for j in range(len(X[i])):
            
            X2.append(X[1][j])
            
            lowesttemp = min(X2)
            
    return lowesttemp


getData(X)

highaverage = averageHigh()

lowaverage = averageLow()

highesttemp = highTemp()

lowesttemp = lowTemp()

print("List of highest and lowest temperatures for each month of the year")

for i in range(len(X)):
    
    for j in range(len(X[i])):
        
        print(X[i][j], " ", end= "")
        
    print()

    
print(" ")

print("Average high temperature for the year", highaverage)


print("Average low temperature for the year", lowaverage)


print("Highest high temperature for the year", highesttemp)


print("Lowest low temperature for the year", lowesttemp)
