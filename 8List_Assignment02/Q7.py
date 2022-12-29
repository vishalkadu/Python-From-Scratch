# 7.  Write a program to create a new list from existing list which contains cube of each number of list. 
data = [911,2,3,4,56,899]
cube_data = []
for i in range(0,len(data)):
    cube_data.append((data[i])**3)
print("New list from existing list",data,"which contains cube of each number of list is,\n",cube_data)