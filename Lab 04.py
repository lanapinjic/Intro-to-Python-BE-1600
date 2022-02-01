def function_1(firstNUM, secondNUM):
    print("print all Numbers:")
    for x in range (firstNUM,secondNUM+1):
        print(x, end = " ")


def function_2(firstNUM,secondNUM):
    print("\nprint all odd Numbers:")
    for x in range (firstNUM, secondNUM+1):
        if x % 2 != 0:
            print (x,end= " ")

def function_3(firstNUM,secondNUM):
    print("\nPrint sum of the even numbers:")
    totalValue =0
    for x in range (firstNUM, secondNUM+1):
        if x % 2 == 0:
            totalValue += x
    print(totalValue)

def function_4(firstNUM,secondNUM):
    print("Print sum of the square of the odd numbers:")
    totalValue =0
    for x in range (firstNUM, secondNUM+1):
        if x % 2 != 0:
            totalValue += x**2
    print(float((totalValue)))


firstNUM = int(input("Enter an odd number "))
secondNUM = int(input("Enter another number "))
 

function_1(firstNUM,secondNUM)
function_2(firstNUM,secondNUM)
function_3(firstNUM,secondNUM)
function_4(firstNUM,secondNUM)

