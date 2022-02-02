testKey1= "zywvutsrqponmlkjihgfedcba"
def subtitutionDecrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plaintext = plaintext.lower()
    oricipher = ""
    for ch in plaintext:
        x = key.find(ch)
        oricipher = oricipher + alphabet[x]
    return oricipher
print("Ciphertext: gsv jfrxp yildm ulc")
print("PlainText: ", subtitutionDecrypt("gsv jfrxp yildm ulc",testKey1))
