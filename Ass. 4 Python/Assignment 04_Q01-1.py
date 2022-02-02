import random
thefile = input("Enter the name of the file to which results should be written: ")

file = open("randomNumbers.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    file.write(line)
    print(line)

file.close()

