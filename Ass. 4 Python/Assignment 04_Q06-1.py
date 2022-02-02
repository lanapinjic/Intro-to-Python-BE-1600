onen = int(input("enter a number: "))
twon = int(input("enter another number: "))
print("the sum of the numbers you entered is: ", float(onen + twon))
x = input("Do you want to do that again? (y/n): ")
while x != "n":
    onen = int(input("enter a number: "))
    twon = int(input("enter another number: "))
    print("the sum of the numbers you entered is: ", float(onen + twon))
    x = input("Do you want to do that again? (y/n): ")
