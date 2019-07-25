"""Write a program to count the number of unique words and the number of occurrences of each of those words from the question provided below.
Input:How much wood would a woodchuck chuck if the woodchuck could chuck wood?"""

data= "How much wood would a woodchuck chuck if the woodchuck could chuck wood"

lst = []
lst=data.split(" ")
c_names={ }
for name in lst:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]=c_names[name]+1
lst1=(c_names.values)
count=0
for k,value in c_names.items():
    if value==1:
        count+=1
    elif not value < 2:
        print(f"{k}:{value} times")

print(f"No. of unique words: {count}")
        