"""Write a program to accept an input string from the user and determine the vowels in the string and calculate the number of vowels. (Hint: Use filter method.)
Input: quintessential
Output: ['u', 'i', 'e', 'e', 'i', 'a']; 6"""

name = input('Enter your name:')
lst=('a','e','i','o','u')
n_lst=[ ]
n_lst=list(filter(lambda x:x in lst , list(name)))
print(n_lst)
c= len(n_lst)
print(f"Count of vowels: {c}")


