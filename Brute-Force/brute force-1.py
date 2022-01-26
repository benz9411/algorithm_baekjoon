M,N=map(int,input().split())

x=input().split()
result=[]

a=0

for i in range(len(x)):
    x[i]=int(x[i])

for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            sum=x[i]+x[j]+x[k]
            result.append(sum)


d=[]
for i in range(len(result)):
    if result[i]<=N:
        b=result[i]
        d.append(b)


print(max(d))
        
