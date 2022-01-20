a=int(input())
sum=0

for i in range(1,a+1):
    sum+=i
    if(i%3!=0):
        print(i,end=' ')

