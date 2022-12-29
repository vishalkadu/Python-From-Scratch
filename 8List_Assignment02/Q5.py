#5.  Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.
data = [23,78,90,67,45,1,8,1,1,1]
input =  int(input("Enter number to check if this element is present: "))
count = 0
for i in data:
    if input == i:
        count += 1
if count > 0:
    print("Given no",input,"exist",count,"times")       
else:
    print("Given no",input,"not exist")  
