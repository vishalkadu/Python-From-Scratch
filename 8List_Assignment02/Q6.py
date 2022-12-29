# 6.  Write a program to remove duplicates from the list. 
data = [23,78,90,67,45,1,8,1,1,1]
new_data = []
count = 0
for i in range(0,len(data)):
    if data[i] not in new_data:
        new_data.append(data[i])
print("List without duplicates: ",new_data)


'''
OR

data = [23,78,90,67,45,1,8,1,1,1]
data = set(data)
print("List without duplicates: ",data)

'''