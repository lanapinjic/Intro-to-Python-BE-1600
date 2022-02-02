
def worldseries():
    x = 1
    go = 1
    dict = {}
    myvalues = {}


    myfile = open("WorldSeries.txt", "r")
    mylines = myfile.readlines()
    for number, line in enumerate(mylines):
        phr = line
        if phr in line:
            linenum = number
            dict[linenum] = line


    for i in dict.values():
        myvalues[i] = 1 + myvalues.get(i, 0)



    while go == 1:
        start = input("Enter a year in the range 1903-2020: ")
        x = int(start)


        
        if x == 1903 or x in range (1905,2004) or x in range(2005,2021):
            a = x-1903
            print("The team that won the world series in ", x, " is the ", dict[a])
            print("They won the world series ",myvalues[dict[a]], "times")
            y = input("Do you want to continue, type 'y' for yes, 'n' for No \n")
            
            if y == 'y':
                go = 1
                
            elif y == 'n':
                print("The program has ended")
                go = 0




                
        if x ==1904 or x == 2004:
            a = x-1903
            print("The world series wasn't played in the year", x)
            y = input("Do you want to continue, type 'y' for yes, 'n' for No \n")
            
            if y == 'y':
                go = 1
                
            elif y == 'n':
                print("The program has ended")
                go = 0



                
        if x not in range(1903, 2021):
            print("The data for the year", x, "is not included in our database")
            y = input("Do you want to continue, type 'y' for yes, 'n' for No \n")
            
            if y == 'y':
                go = 1
                
            elif y == 'n':
                print("The program has ended")
                go = 0



                

worldseries()
            
