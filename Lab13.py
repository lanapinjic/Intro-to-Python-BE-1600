
L = [[-2, 3, -5],
     [-8, 4, -6],
     [9, -3, 77],
     [11, -2, 9]]

print("2D List")
for i in range(len(L)):
    for j in range(len(L[i])):
        print("{0:2d}".format(L[i][j]), end= " ")
    print()

def main(L):
    L2 = []
    acc = 0
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] < 0 and L[i][j] % 2 != 0:
                acc += 1
        L2.append(acc)
        acc = 0
    print("\nNumber of odd negative values")
    print("Col 1 : ", L2[1])
    print("Col 2 : ", L2[0])
    print("Col 3 : ", L2[2])
    return L2

main(L)
            
