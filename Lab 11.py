#writing the txt file then closing it
numbers = open("numbers.txt","w")
numbers.write("Dan 3 \n")
numbers.write("Cordelia 7 \n")
numbers.write("Tanner 14 \n")
numbers.write("Mellany 13 \n")
numbers.write("Curtis -4 \n")
numbers.write("Amy 12 \n")
numbers.write("Nick 6 \n")
numbers.write("Tina 4 \n")
numbers.write("Jack -13 \n")
numbers.write("Sarah 12 \n")
numbers.write("Robert -2 \n")
numbers.close()
#opening the text file again to read it 
numbers = open("numbers.txt", "r")
# negcount = negative count, negsum = negative sum, poscount = positive count, possum = positive sum
negcount = 0
oddcount = 0
negsum = 0 
poscount = 0
possum = 0
for aline in numbers:
    if aline != "\n":
        aline = aline.strip().split()
    number = int(aline[1])
    if number <0:
        negcount +=1
        negsum += number
        if number % 2 != 0:
            oddcount +=1
    else:
        poscount = poscount+1
        possum = possum+number
        if number % 2==1:
            oddcount +=1
print("negative count = ", negcount)
print("odd count = ", oddcount)
print("negative sum = ", negsum)
print("positive average = ", str(possum/poscount))

numbers.close()

