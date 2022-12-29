#8.  Write a program to create a duplicate of an existing list. It should not point to same list. 
data = [20,67,89,23,45,2,237]
data_duplicate =[]
for i in data:
    data_duplicate.append(i)
print("Duplicate of existing list is,",data_duplicate)


'''
#OR
data = [20,67,89,23,45,2,237]
data_duplicate = data.copy()
print("Duplicate of existing list is,",data_duplicate)'''