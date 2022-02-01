s = input("Enter a string: ")
s = s.upper()
s = list(s)
d = {}
for a in s:
    if a not in d:
        d[a] = 1
    else:
        d[a] += 1
for y,z in d.items():
    z1 = "*" * z
    print(y,z1)






