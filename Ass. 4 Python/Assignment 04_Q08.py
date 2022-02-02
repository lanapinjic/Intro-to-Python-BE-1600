def print_average():
    x = float(input("enter a number: "))
    if x >= 0:
        t = 0
        c = 1
        t = t + x
        while x>= 0:
            x = float(input("Enter a number: "))
            t = t + x
            c = c + 1
        c = c -1
        t = t - x
        avg = t/c
        print("Average was ", avg)
    else:
        print("Average was 0:")
print_average()
