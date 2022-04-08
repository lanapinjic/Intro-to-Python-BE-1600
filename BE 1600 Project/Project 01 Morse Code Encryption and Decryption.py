def function():
    #function for loading morse code into the dictionary
    dictm = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-', " " : " ", "":""}

    #function for printing the menu 
    def menu():
        print("Hello, this program allows you to translate text to morse code or translate morse code to text\n")
        print("Please, select one of the below options: \n")
        print("*** Enter 't' for encoding text \n*** Enter 'm' for decoding morse code \n*** Enter 'e' to exit the program.")
        #closing the function as we wont need any of the information later 
    menu()




    # english to morse code, selection 't'
    def encrypt(message):
        code = ''
        for letter in message:
            if letter != ' ':
                #goes into the dictionary and adds the morse code for each letter
                #with the space to the seperate out the characters 
                code += dictm[letter] + ' '
            else:
                #1 space = dif characters
                # 2 spaces = dif words 
                code += ' '
        return code
     

    # from morse to english, selection 'm'
    def decrypt(message):
     
        # extra space added at the end to access the
        # last morse code
        message += ' '
        decipher = ' '
        ctxt = ''
        for letter in message:
            # checks for spaces in the text
            if (letter != ' '):
                # counter to track the spaces
                i = 0
                # storing the morse code letter by letter
                ctxt += letter
            # what to do when it encounters a space
            else:
                #shows new character
                i += 1
                if i == 2:
                #shows new word:
                    decipher += ' '
                
                else:
                    # searching for the keys using their values (reverse of encryption)
                    decipher += list(dictm.keys())[list(dictm
                    .values()).index(ctxt)]
                    ctxt = ''
     
        return decipher


    #main function where the user input is used then they either encrypt, decrypt or exit the program. 
    def mainfunc():
        text = input("My input is: ")
        #the user input gets encrypted here using the information above 
        if text == str('t'):
            message = input("Please enter text to translate: \n")
            result = encrypt(message.upper())
            print(result)
        #the user input gets decrypted here using the information above 
        elif text == str('m'):
            message = input("Please enter morse to translate: \n")
            resulttwo = decrypt(message)
            print(resulttwo)
        #the user input allows for the program to end here 
        elif text == str('e'):
            print("Thanks for using this program!")

            
        #what to do if they dont input 't', 'm', or 'e'
        #creating an infitine loop until a valid option is given
        elif ('m'or't'or'e') not in text:
            while text != 'm' and text !='t' and text != 'e':
                #what keeps displaying if a valid option is not given
                text = input("***invalid option***\nPlease enter a valid option: ")
                #if a valid option is now given it will reroute to the options below
                if text == 'm' or text == 't' or text == 'e':
                    #same process as above just adding a break to stop the loop for all below
                    if text == ('t'):
                        message = input("Please enter text to translate: \n")
                        result = encrypt(message.upper())
                        print(result)
                        break
                    if text == ('m'):
                        message = input("Please enter morse to translate: \n")
                        resulttwo = decrypt(message)
                        print(resulttwo)
                        break
                    if text == ('e'):
                        print("Thanks for using this program!")
                        break
        #allowing the main function to work
    if __name__ == '__main__':
        mainfunc()
        
#closing the first function
function()
