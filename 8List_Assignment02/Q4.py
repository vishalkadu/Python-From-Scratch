# 4.  Write a program to reverse the list.

data = [22, 45, 8, 99, 1, 3]
rev_data = []
for i in data:
    rev_data = [i] + rev_data
print("Given list: ", data)
print("Revere of list: ", rev_data)


'''data = [22, 45,8,99,1,3]
data.reverse()
print("Reverse of given list is,",data)'''
