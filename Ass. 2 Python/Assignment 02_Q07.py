word = input("Enter a word : ")
repetition = int(input("Enter the Number of Repetitions : "))

def repl(word, rep):
    results = ""
    for x in range(rep):
        results = results + word

    if (repetition < 0):
        print("")
        
    return results

space = (" -> ")
print(word + space +(repl(word, repetition)))
