'''
4. Python Program to Find the Second Largest Number in a List Using 
Bubble Sort
'''

data = [12,1,4,89,22,57]
def bubblesort(data):
    n = len(data)
    for i in range(1, n):  
        for j in range(0, n - i): 
            if (data[j] > data[j+1]): 
                data[j], data[j+1] = data[j+1], data[j] 
    return data
print("Sorted list: ",bubblesort(data))
print("Second largest element",data[-2])