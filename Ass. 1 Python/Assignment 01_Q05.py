def function_1(a):
    print("Income from class A seats: $",a*15, end = " ")


def function_2(b):
    print("\nIncome from class B seats: $",b*12, end = " ")


def function_3(c):
    print("\nIncome from class C seats: $",c*9, end = " ")



def function_4(a,b,c):
    print("\nTotal Income: $",(a*15)+(b*12)+(c*9), end = " ")


a = int(input("Enter count of A seats: "))
b = int(input("Enter count of B seats: "))
c = int(input("Enter count of C seats: "))
 

function_1(a)
function_2(b)
function_3(c)
function_4(a,b,c)
