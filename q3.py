num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print(f"prime numbers between {num1} and {num2} are:")
for num in range(num1,num2+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
     