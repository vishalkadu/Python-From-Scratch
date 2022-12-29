'''
3. Python Program to Sort the List According to the Second Element in 
Sublist
'''
data = [['a',2],['b',1],['d',4],['e',89],['f',22],['g',57]]

def bubblesort(data):
    n = len(data)
    for i in range(1, n):  
        for j in range(0, n - i): 
            if (data[j][1] > data[j+1][1]): 
                data[j][1], data[j+1][1] = data[j+1][1], data[j][1]
    return data
print("Sorted list: ",bubblesort(data))