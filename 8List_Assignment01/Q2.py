# 2. Python Program to Merge Two Lists and Sort it
data1 = [2,1,4,89,22,57]
data2 = [33,56,78,23,90]
data1.extend(data2)
print(data1)
def bubblesort(data1):
    n = len(data1)
    for i in range(1, n):   
        for j in range(0, n - i): 
            if (data1[j] > data1[j+1]): 
                data1[j], data1[j+1] = data1[j+1], data1[j] # swap logic 
    return data1
print("Merged and sorted list: ",bubblesort(data1))