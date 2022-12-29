# 2.  Write a program to find maximum and minimum element in a list. 
data = [99,12,345,567,67,78,90,34]
fmin= data[0]
fmax = data[0]
for i in range(1,len(data)):
    if fmin > data[i]:
        fmin = data[i]
    if fmax < data[i]:
        fmax = data[i]
print("Minimum no: ",fmin)
print("Maximum no: ",fmax)







'''
# or 
print("Minimum no: ",min(data))
print("Maximum no: ",max(data))'''