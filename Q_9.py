"""Write a program to find the word(s) that occur maximum and minimum number of times in the given paragraph. Also, display those words next to their respective count.
Input:
"Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3."
Output:
Word appearing maximum times: abcdefg; x times
Word appearing minimum times: pqrstuv; y times
(Where abcdefg and pqrstuv are words from the given paragraph; x and y are the number of instances these words appear in the paragraph.)"""

data = "Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3"
lst = []
lst=data.split(" ")
#print(lst)
c_names={ }
for name in lst:
    if c_names.get(name)==None:
        c_names[name]=1
    else:
        c_names[name]=c_names[name]+1
lst1=(c_names.values)
#print(c_names)
count=0
lst_value=[] 

for k,value in c_names.items():
    lst_value.append(value)
#print(lst_value)

max_val=max(lst_value)
#print(max_val)
min_val=min(lst_value)
#print(min_val)
max_lst=[]
min_lst=[]
for k,value in c_names.items():
    if value==max_val:
        max_lst.append(k)
        
    elif value==min_val:
        min_lst.append(k)
    else:
        pass

print(f"The items with max_count are:{max_lst} and max_count is:{max_val}")
print(f"The items with min_count are:{min_lst} and min_count is:{min_val}")

