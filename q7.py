def sumof(num):
    sum=0
    while num!=0:
        sum+=num%10
        num//=10
    print(sum)
    return sum
num=int(input("enter the number"))
temp=num
while True:
    sum=sumof(num)
    if sum//10==0:
        break
        else:
            num=sum
            