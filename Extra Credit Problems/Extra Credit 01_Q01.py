s = "ABCDEFGHI"
def thecipher(s):
    for x in range(3):
        railone = ""
        railtwo = ""
        railthree = ""
        for i in range (0, len(s), 3):
            railone += s[i]
            railtwo += s[i+1]
            railthree += s[i + 2]
        newstr = railthree + railtwo + railone
    print(newstr)

thecipher(s)
