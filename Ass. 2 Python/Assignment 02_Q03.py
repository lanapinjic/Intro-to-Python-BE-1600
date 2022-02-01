#loop #total #starts at 1/30 to 30/1

num = 1
denom = 30
sum = 0

for x in range(30):
    a = (num/denom)
    num += 1
    denom -= 1
    sum = a + sum


print(sum)
