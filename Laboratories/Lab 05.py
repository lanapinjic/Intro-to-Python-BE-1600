def f():
    numDays = int(input("Enter the number of days: "))
    print("Day   Pennies")
    print("------------------------")
    acc = 0
    r = 0.005
    for x in range(1,numDays + 1):
        acc = acc + r
        r = r*2
        print(x, "    $", r)
    print("The total salary for", numDays, "days is: $", round(acc*2,2))

f()
