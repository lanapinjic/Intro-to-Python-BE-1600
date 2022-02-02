def main():
    print("Fahrenheit Celcius")
    f = -10.00
    header = "Fahrenheit Celcius"

    with open ("tempconv.txt","a") as my_file:
        my_file.write(header+"\n")
        for i in range (21):
            c = (f-32)/1.80
            print("{:.2f}".format(f), " ", r"{:.2f}".format(c))
            my_file.write("   " + str("{:.2f}".format(f))+"\t\t"+str("{:.2f}".format(c))+"\n")
            f = f + 1
        my_file.close()
main()
