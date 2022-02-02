import random 

k = random.randint(2,10)
print(k)
numbs = []

for x in range(k):
    print("Enter a Value",(x+1), ": ", end="")
    num = int(input())
    numbs.append(num)

    
def collapse(list):
    c_list = []
    for index in range(0, len(list), 2):
        if (len(list)%2 == 0):
            c_list.append(list[index] + list[index+1])
        else:
            if x == (len(list)-1):
                c_list.append(list[index])
                continue
            c_list.append(list[index] + list[index+1])
    print("Old List:",list)
    print("Collapse List:",c_list)
    
collapse(numbs)
