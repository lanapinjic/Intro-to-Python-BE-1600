txt = input("Enter a word, phrase or sentence :")

def word_count(txt):
    x = txt.split()
    print(txt)
    words = str(len(txt.split()))
    space = (" -> ")
    print("'",txt,"'",space, words)

word_count(txt)
