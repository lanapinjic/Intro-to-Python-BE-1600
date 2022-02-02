import random

package = random.randint(1,150)
print("Number of Packages Purchased: ", package)


y= (package *25)
a = y *0.2
b = y *0.3
c = y *0.4
d = y *0.5

if package <= 9:
    print("Discount Amount: $ 0")
    print("Total Amount : $", y)


if package >= 10 and package <= 19:
    print("Discount Amount: $", a)
    print("Total Amount : $", y-a)


if package >= 20 and package <= 49:
    print("Discount Amount: $", b)
    print("Total Amount : $", y-b)



if package >= 50 and package <= 99:
    print("Discount Amount: $", c)
    print("Total Amount : $", y-c)


if package >= 100 and package <= 150:
    print("Discount Amount: $", d)
    print("Total Amount : $", y-d)

