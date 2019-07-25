"""Write a program to accept a two-dimensional array containing integers as the parameter and determine the following from the elements of the array:
a.	element with minimum value in the entire array
b.	element with maximum value in the entire array
c.	the elements with minimum and maximum values in each column
d.	the elements with minimum and maximum values in each row
[[0 1 2 3]
 [3 4 5 5]
 [6 7 8 8]
 [9 0 1 9]]"""

lst = [[0,1, 2, 3],[3, 4, 5, 5],[6, 7 ,8 ,8],[9, 0, 1, 9]]
all_nums=[j for i in lst for j in i ]
print(all_nums)
#to print the max element
maxi = max(all_nums)
mini = min(all_nums)
print(f"Maximum ={maxi} and Minimum={mini}")
sum_lst=[]

min_col=list(min(map(lambda x:x[i],lst)) for i in range(4))
print(f"Minimum column value: {min_col}")
max_col=list(max(map(lambda x:x[i],lst)) for i in range(4))
print(f"Maximum column value: {max_col}")
min_row=list(map(lambda x:min(x),lst))
print(f"Minimum column value:{min_row}")
max_row=list(map(lambda x:max(x),lst))
print(f"Maximum column value:{max_row}")











