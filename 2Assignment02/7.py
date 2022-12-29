# 7. Write a program to check if given 3 digit number is a palindrome or not.
number = int(input("Enter a 3 digit number: ")) #e.g. 121
print("Given number is",number)
digit3 = number % 10 #1
number //= 10 #12
number //= 10 #1
if digit3 == number:
    print("Given number is a palindrome number.") 
else:
    print("Given number is not a palindrome number.") 