
widtha = int(input("Enter a width for rectangle A: "))
lengtha = int(input("Enter a length for rectangle A: "))

widthb = int(input("Enter a width for rectangle B: "))
lengthb = int(input("Enter a length for rectangle B: "))
 

areaa = widtha * lengtha
areab = widthb * lengthb

print("Area A: ", areaa )
print("Area B: ", areab )


if (areaa > areab):
    print("Area A is greater than Area B")

if (areaa < areab):
    print("Area B is greater than Area A")

if (areaa == areab):
    print("Area A is equal to Area B")


