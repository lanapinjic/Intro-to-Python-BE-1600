import math

a = open("data.txt", 'r')
X = []

for myline in a:

    myline = myline.split(" ")
    
    x = float(myline[0])
    y = float(myline[1])
    X.append([x,y])

a.close()

def dist(p1,p2):
    
    d = math.sqrt((p1[0] -p2[0])**2 + (p1[1] - p2[1])**2)
    
    return d


x = "{0:6}{1:6}{2:6}{3:6}{4:6}{5:6}{6:6}{7:6}{8:6}".format("P1","P2","P3","P4","P5","P6","P7", "P8")

print(x)

disttwo = []

for i in range(len(X)):
    
    disttwo.append([0]*8)

for i in range(len(X)):
    
    for j in range(len(X)):
        
        disttwo[i][j] = dist(X[i],X[j])

for i in range(len(X)):
    
    print("P{0:<5}{1:<6.2f}{2:<6.2f}{3:<6.2f}{4:<6.2f}{5:<6.2f}{6:<6.2f}{7:<6.2f}{8:<6.2f}".format(i+1), disttwo[i][0],disttwo[i][1],disttwo[i][2],disttwo[i][3], disttwo[i][4],disttwo[i][5],disttwo[i][6], disttwo[i][7]))     
        
