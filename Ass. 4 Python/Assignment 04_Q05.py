my_file = open('books.txt','r')
f = my_file.read(lines)
my_file.close()

d={}

for i in f:
    i = i.strip()
    b,a= i.split(',')
    if a in d:
        d[a] = [d[a],b]
    else:
        d[a] = [b]
for i in d.keys():
    print('{}, {}'.format(i,d[i]))
