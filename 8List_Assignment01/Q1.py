'''Q1. Python Program to Put Even and Odd elements of a List into two 
Different Lists'''

main_list = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for i in main_list:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even no from list:",even)
print("Odd no from list:",odd)