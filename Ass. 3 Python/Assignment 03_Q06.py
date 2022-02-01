import math

a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
c = int(input("Enter a Number: "))
d = int(input("Enter a Number: "))
e = int(input("Enter a Number: "))
f = int(input("Enter a Number: "))
g = int(input("Enter a Number: "))
h = int(input("Enter a Number: "))
i = int(input("Enter a Number: "))
j = int(input("Enter a Number: "))

my_list = [a , b , c , d , e , f , g , h , i , j]


my_list.sort()
print("Low: ", float(*my_list[:1]))
print("High: ", float(my_list[-1]))
print("Total :", float(sum(my_list)))

avg = sum(my_list)/len(my_list)
print("Average: ", round(avg,2))
