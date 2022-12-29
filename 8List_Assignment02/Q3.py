# 3.  Write a program to find the second largest element in the list.
data = [11,34,56,89,45,67]
fmax= data[0]
smax = 0
for i in range(1,len(data)):
    if fmax < data[i]:
        smax = fmax 
        fmax = data[i]
    elif smax < data[i]:
        smax = data[i]
print("Second largest number from list: ",smax)