
def palin(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp!=rev):
        return True
        #print("The number is palindrome!")
    else:
        False
        #print("Not a palindrome!")
        

A=[]
n=int(input())
m=int(input())

for i in range(1,50):
    if(i<10):
        a=11*i
        A.append(a)
    elif(i<20):
        a=111*(i-10)
        A.append(a)
    elif(i<30):
        a=1111*(i-20)
        A.append(a)
    elif(i<40):
        a=1111*(i-30)
        A.append(a)
    else:
        a=11111*(i-40)
        A.append(a)
            
print(A) 
A = [i for i in A if i != 0]
#print(A)
for i in range(len(A)):
    if((n<=(pow(A[i],3))<=m) and palin(pow(A[i],3))):
        print(pow(A[i],3),A[i])
#print(B)        

G = []
for i in range(2,6):
    for j in range(2,10):
        d = int(j*((pow(10,i) - 1)/(10-1)))
        G.append(d)
print(len(A))
print(len(G))    
if(G==A):
    print("ok")

