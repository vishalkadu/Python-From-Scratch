list1 = [1,2,3,56,78,9,67,'hi']
list2 = [1,2,'hi','how',67,'are',9,'you!!']
list_int =[]

for i in list1:
    if i in list2:
        list_int.append(i)
print("Lists intersection: ",list_int)