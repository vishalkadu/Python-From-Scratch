# 1. Write a program to check if the given number is positive or negative.
number = int(input("Enter a number: "))
if number%2 == 0:
    print("Number",number,"is positive")
else:
    print("Number",number,"is negative")