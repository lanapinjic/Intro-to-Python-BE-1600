txt = input("Enter a string: ")
vowel = "aeiouAEIOU"
con = "bcdfghjklmnpqrstvwzBCDFGHJKLMNPQRSTVWZ"


def argument1(txt):
    vowel_num = 0
    for x in range(len(txt)):
        if txt[x].isalpha():
            if txt[x] in vowel:
                vowel_num += 1
    print("The string you entered includes ", vowel_num, "vowels and ", end="")
                


def argument2(txt):
    con_num = 0
    for x in range(len(txt)):
        if txt[x].isalpha():
            if txt[x] in con:
                con_num += 1
    print(con_num, "consonants")

argument1(txt)
argument2(txt)
            
