'''
Q5. Write a program to check if a given number is Fibonacci number.
 Example:
 Input : 8
 Output : Yes
 Input : 34
 Output : Yes
 Input : 41
 Output : No
Hint: A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 - 4) is a perfect
square
'''
def CheckFibo(n):
    x = (5*n**2 + 4) 
    y = (5*n**2 - 4)
    if x**0.5 == int(x**0.5) or y**0.5 == int(y**0.5) :  # x.0 == int(x.0) -> True
        print("Yes,given number is fibonacci number")
    else:
        print("No,given number is not a fibonacci number")
n = int(input("Enter a number: "))
CheckFibo(n)



