MaxSIZE = 256
def getMaxOccuringChar(str):
    count = [0] * MaxSIZE
    max = -1
    a = ''

    for i in str:
        count[ord(i)]+=1;
 
    for i in str:
        if max < count[ord(i)]:
            max = count[ord(i)]
            a = i
    return a

str = input("Enter a string: ")
print ("The character that appears most frequently in the string is " + getMaxOccuringChar(str).upper())
