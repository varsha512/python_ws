nterms=10
n1=0
n2=1
count=0
if nterms<=0:
    print("please enter a positive integer")
elif nterms==1:
    print(f"fibonacci series upto {nterms}:")
    print(n1)
else:
    print(f"fibonacci series upto {nterms}:")
    while count<nterms:
        print(n1,end=',')
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1

