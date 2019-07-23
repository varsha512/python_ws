num=int(input("enter the no:"))
while True:
    if(num>1):
        for i in range(2,n+1):
            sum+=1/i**3
        print(f"sum {sum}")
        break
    else:
        num=int(input("enter the number greater than 1"))