num=int(input())

ten,one,sum,i,sumz=0,0,0,0,0


if num>10:
    num*=10
    sum=num
    while True:
        ten=sum//10
        one=sum%10
        sum=(one*10)+(ten+one)
        i+=1
        if num==sum:
            break
        print(i)

else:
    sum=num
    while True:
        ten=sum//10
        one=sum%10
        sumz=ten+one
        if sumz>=10:
            sumz=sumz%10
        else:
            sum=(one*10)+sumz
        i+=1
        if num==sum:
            break
        print(i)
        
