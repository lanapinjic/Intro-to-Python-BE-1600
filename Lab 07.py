def main():
    string = input("Enter a string ")
    string = string.upper()
    
    ##prints old string
    print("Old String: " + string)
    
    count = 0

    #replaces lowercase
    for x in range(0,len(string)):
        if((string[x]!= "a") & (string[x]!= "e") &(string[x]!= "i" )&(string[x]!= "o" )&(string[x]!= "u")&(string[x]!=" ")
           & (string[x]!= "A")& (string[x]!= "E")& (string[x]!= "I")& (string[x]!= "O")& (string[x]!= "U")):
            count = count +1
            
    #replaces upper case + takes away first and last letter  
    for x in range(0, len(string)):
        if((string[x]!= "A")& (string[x]!= "E")& (string[x]!= "I")& (string[x]!= "O") & (string[x]!= "U")&(string[x]!=" ")):
            string = string.replace(string[x],"*")
    
    print("New String: " + string[1:-1])
    print("Number of Consonants Characters:", end=" ")
    print(count-1)
main()
