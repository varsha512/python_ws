import math

def is_prime_fun(num):
    '''if given num is prime it return true otherwise false'''
    if num<2:
        is_prime=False
    else:
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                return False
    return True
    
num=int(input("enter the number:"))
is_prime=is_prime_fun(num)


if is_prime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
