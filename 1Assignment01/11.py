# Find the sum of three digit number. 

# method 01
number = int(input("Enter a three digit number: "))
two_digit = number//10 
digit1 = two_digit//10
digit2 = two_digit%10
digit3 = number%10
sum = digit1 + digit2 + digit3
print("Sum of 3 digit number",number,"is",sum)

# method 02
number = int(input("Enter a three digit number: ")) #e.g number = 123
sum = 0
sum += number % 10 # sum = sum + number%10, here sum = 3
number//=10 # number = number//10 ,here number = 12
sum += number // 10 # sum = sum + number // 10, here sum = 3 + 1
sum += number % 10  # sum = sum + number % 10, here sum = 3 + 1 + 2
print("Sum of 3 digit number is",sum)