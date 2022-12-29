'''
Q1. Write a program to print all divisors of given number.
Example:
Input: 6
Output: 1 2 3 6
'''
def divisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i,end=" ")

n = int(input("Enter a number: "))
print("Divisors of given number",n,"are,",end=" ")
divisors(n)
