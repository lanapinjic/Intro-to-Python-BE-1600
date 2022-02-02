def dictionary():
    try:
        #open the file at the very beginning
        y = open("mail.txt", "r")
    except:
        #if the file is empty then we will be able to write it 
        y = open("mail.txt","w")
    #d represents the dictionary we will be storing all the information in
    d = {}
    #opening the txt file and reading it
    #copying that file into the dictionary so they are intertwined 
    with open("mail.txt") as my_file:
        for line in my_file:
            (varn,varm) = line.split()
            #representing throu keys and values
            #name will be the key and email will serve as the values 
            d[varn] = varm 
        return d

#starting the options for choice one which is to look up an email address
def choiceone(object):
    #accessing the dictionary
    d = dictionary()
    #if the name equals the object it will identify it as found and return it as true
    for name, mail in d.items():
        if(name==object):
            print("Found!")
            print("\nName: ",name,"\nEmail: ",mail,"\n")
            return(True)
        #if not found then it will print the following and will be understood as false
    print("The specified name was not found\n\n")
    return(False)


def choicetwo():
    #accessing the dictionary
    d = dictionary()
    #allowing the user input for the name and emai
    varn = input("Enter Name: ")
    varm = input("Enter Email: ")
    #allows for you to string together the name and email into a string with a space in the middle
    string = (str(varn+' '+varm))
    valid = True
    #valid associated to the true boolean expression
    for name, mail in d.items():
        #identifies to see if the name inputed matches one in the dictionary
        if(varn==name):
            print("That name already exists\n")
            valid = False
        #identifies to see if the email inputed matches one in the dictionary
        if(varm==mail):
            print("That email already exists\n")
            valid = False
        #But if there are no matches we will associate it with being true that they can add a name and email and so will now edit the dictionary to write a new name and email (key and value)
        
    if valid:
        print("Name and email address have been added.\n")
        with open("mail.txt","a") as w:
            #remeber string = (str(varn+' '+varm)) from line 42
            w.write(string+ "\n")
            #the key will be variable n (name) and the value will be variable m (email)
            d[varn] = varm
    return d


def choicethree():
    #accessing the dictionary
    d = dictionary()
    #creating a specific user input
    varn = input("Enter Name: ")
    #specifiying what elements we are looking for in the dictionary
    if(choiceone(varn)):
        for name, mail in d.items():
            #accepts user input for new email, if the key associated with the email (value) as been identified than we know an email address exists that the user can then change it
            if(varn==name):
                d[varn] = input("Enter the new email: \n")
#this is how we edit that now email by opening up the dictionary and writing it (editing it)
        with open("mail.txt", "w") as my_file:
            for name, mail in d.items():
                print(name, ' ', mail, my_file)
        print("Information updated\n")

def choicefour():
    #accessing the dictionary
    d = dictionary()
    #allowing for user input for the key(name) in the dictionary
    varn = input("Enter Name: ")
    if((varn)):
        #if there is a equal name in the dictionary as the one that the user inputs then it will remove it from the dictionary
        for name, mail in d.items():
            if(varn==name):
                remove=name
                print("Information Deleted!\n")
                #hence here we will remove that specific key from the dictionary 
        del d[remove]
#opening the dictionary and editing it
        with open("mail.txt", "w") as my_file:
            for name, mail in d.items():
                print(name, ' ', mail, my_file)
#setting up the menu and labeling a variable as choice to represent the users first input
def mainmenu():
    print("Menu\n-----------------------------")
    choice = input("1. Look up an email address \n2. Add a new name and email address \n3. Change an exisiting email adress \n4. Delete a name and email address \n5. Quit the program \nEnter your choice:")
    choice = int(choice)

    
    #if they include a number that is not 1-5 then it will send a message saying its not an option
    if(choice!=5 and choice!=4 and choice!=3 and choice!=2 and choice!=1):
        print("Invalid Option")
        mainmenu()
    #if the choice is equal to one then it will only execute this if and will ignore the elif's
    if (choice==1):
        # cannot put this directly under the first function for choice 1 like the others as you must identify the name here and what user input it belongs to
        name = input("Enter a name: ")
        choiceone(name)
    #if the choice is equal to two then it will execute the below
    elif (choice==2):
        choicetwo()
    #if the choice is equal to three then it will execute the below
    elif(choice==3):
        choicethree()
    #if the choice is equal to four then it will execute the below
    elif(choice==4):
        choicefour()
    #if the choice is equal to five then it will execute the below
    elif(choice==5):
        print("Information saved")
        return()
    #if it does not equal 5 go to the main menu again
    if (choice!=5):
        #allows for the menu to pop up again after it completes the firs run
        mainmenu()
mainmenu()
