sum=0
Cnt=0

def primenum(x):
    global sum
    global Cnt
    for i in range(2,x):
        if x%i==0:
            sum=1
            break
        else:
            sum=2
    if sum== 2:
        Cnt+=1
    return Cnt
        
    


num=int(input())

a=input().split()

for i in range(num):
    a[i]=int(a[i])
    b=primenum(a[i])

print(sum)



