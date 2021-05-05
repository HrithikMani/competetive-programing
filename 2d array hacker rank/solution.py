import numpy as np
def msum(a):
    a[1][0] = 0
    a[1][2] = 0
    s =0
    for i in range(len(a)):
        for j in range(len(a)):
            s = s + a[i][j]
    return s


def fun(m,x,y):
    slice_x = x
    slice_y =y
    width = len(m[0])
    height = len(m)
    slices = []
    for i in range(0, height - slice_y + 1):
        for j in range(0,width - slice_x + 1):
            slices.append(
                    [
                            [m[a][b] for b in range(j,j+slice_x)]
                            for a in range(i,i+slice_y)
                    ]
                    )
    return slices
    
    


a = np.random.randint(0,2,size=(4,4))
print(a)
print("\n")
b = fun(a,3,3)
for i in range(len(b)):
    print(b[i])
    s = msum(b[i])
    
    print(s)

'''

b = len(a)
i= 0
c = []
j=0
while(i<b-1):
    print(i)
    if((i+3) <= b):
        while(j<i+2):
            c.append(a[j][i:i+3])
            j=j+1
        print(c)
        c = []
        print(j)
        j = 0        
    i = i + 1
    print(i)
            
'''

