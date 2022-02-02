import random
def dice_sum():
    x = int(input("Desired Dice Sum: "))
    ran1 = random.randint(1,6)
    ran2 = random.randint(1,6)
    sum = ran1 + ran2
    print(ran1, "and", ran2, "=", sum)
    while sum != x:
        ran1 = random.randint(1,6)
        ran2 = random.randint(1,6)
        sum = ran1 + ran2
        print(ran1, "and", ran2, "=", sum)
dice_sum()
