'''
Q2. Write a program to print sum of all divisors of given number.
Example:
Input: 6
Output: 12
'''
def SumOfDivisors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum

n = int(input("Enter a number: "))
print("Sum of the divisors of given number", n, "is,", end=" ")
print(SumOfDivisors(n))
