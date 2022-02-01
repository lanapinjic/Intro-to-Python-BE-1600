my_dict = {'a':15 , 'c':35, 'b':10}
keys = list(my_dict.keys())
keys.sort()
values = list(my_dict.values())
print("Keys: ", keys)
print("Values: ", values)
print("Key Value Pairs")

for x,y in my_dict.items():
    print(x,y)

print("Key-Value pairs- sorted by key")
for x,y in sorted(my_dict.items()):
    print(x,y)
    
print("Key-Value pairs- sorted by value")
for x in sorted (my_dict.values()):
    print(list(my_dict.keys())[list(my_dict.values()).index(x)],x)

