import random as r

even = 0
odd = 0

for x in range(100):
    number = r.randint(1,100)
    
    if((number % 2) == 0):
        even += 1
    else:
        odd += 1
        
print("Out of 100 random numbers,", odd, "were odd, and", even, "were even.")
