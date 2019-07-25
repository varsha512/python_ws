"""Write a program to add the elements of 2 arrays that are of the same dimension. (Hint: Use map method.)"""
#lst_1=list(input("Enter List 1:"))
lst_1 = [1,2,3,4]
lst_2 = [4,5,6,7]
lst_3 = [ ]
for i in range(len(lst_1)):
    lst_3.append(lst_1[i]+lst_2[i])
print(lst_3)