import random

my_list = random.sample(range(1, 10), 5)

print ("Old List: " + str(my_list))

def swapList(my_list):
     
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
 
    return my_list
     
print("New list after swappping first and last elements in Old List: ", (swapList(my_list)))

print("After reversing New List elements " + str(my_list[::-1]))

