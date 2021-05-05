def mod(a):
    if(a < 0):
        return -1*a
    else:
        return a
def disply(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j],end = " ")
        print("\n")


a = [
     [[8,1,6],[3,5,7],[4,9,2]],
     [[6,1,8],[7,5,3],[2,9,4]],
     [[4,9,2],[3,5,7],[8,1,6]],
     [[2,9,4],[7,5,3],[6,1,8]],
     [[8,3,4],[1,5,9],[6,7,2]],
     [[4,3,8],[9,5,1],[2,7,6]],
     [[6,7,2],[1,5,9],[8,3,4]],
     [[2,7,6],[9,5,1],[4,3,8]]
     ]
b = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
x = []
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i])):
            c = mod(a[i][j][k] - b[j][k])
            a[i][j][k] = c
            s = s + a[i][j][k]
    x.append(s)
    s = 0

print(min(x))            
        
            