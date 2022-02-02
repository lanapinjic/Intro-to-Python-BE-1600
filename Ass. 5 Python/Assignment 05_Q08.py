y = int(input("Enter the number of years:"))

yearcount = 1


for i in range(y):
    acc = 0
    
    count = 0
    
    print("For year", yearcount)
    
    yearcount += 1
#i and j for variables as they go together 
    
    for j in range(12):
        
        print("Enter the rainfaill amount for the month", j+1, ":", end = "")

        y = float(input())
        
        acc += y
        
        count += 1
        
    avg = acc / count


    
print("For", y * 12,"months")

print("Total rainfall:", acc)

print("Average monthly rainfall:", avg)

