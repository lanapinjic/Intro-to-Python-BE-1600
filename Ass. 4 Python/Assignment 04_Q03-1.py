txt = 'This is line'
with open('line_1_to_9.txt','w') as file:
   for num in range(1,12):
      file.write(f'{txt} {num}\n')


f = open('line_1_to_9.txt', 'r')
w = open('thatFile.txt', 'w')
count = 0
for line in f:
   if count % 2 == 0:
       w.write(line)
   count += 1
w.close()
f.close()

f = open('thatFile.txt', 'r')
for line in f.readlines():
    print(line.strip())
    
