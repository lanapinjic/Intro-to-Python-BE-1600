def function_1(a, b):
    for x in range (a,b+1):
        print(x, end = " ")


def function_2(a,b):
    totalValue =0
    for x in range (a, b+1):
        totalValue += x
    totalValue=list(range(a,b))
    
    print("\nsum of numbers:",(sum(range(a, b+1))))


a = 5
b = 10

function_1(a,b)
function_2(a,b)
