# 4. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input("Enter physics marks:")) 
sub2 = int(input("Enter chemistry marks:")) 
sub3 = int(input("Enter mathematics marks:")) 
sub4 = int(input("Enter biology marks:")) 
sub5 = int(input("Enter english marks:")) 
total = int(input("Enter out of marks:")) 
total_sub = sub1 + sub2 + sub3 + sub4 + sub5
percentage = ( total_sub / total ) * 100 
print("Percentage",percentage,"% and class ",end="")
if percentage >= 60:
    print("First class")
elif percentage >= 50 and percentage <= 60:
    print("Second class")
elif percentage >= 40 and percentage <= 50:
    print("Third class")
else:
    print("Fail")

