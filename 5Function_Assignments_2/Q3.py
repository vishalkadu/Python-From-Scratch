'''
Q3. Write a program to check if a given number is perfect or not.
Hint: A number is a perfect number if is equal to sum of its proper divisors, that is, sum of its
positive divisors excluding the number itself.
Example: 6,28,496,8128 are perfect numbers.
'''

def Perfect(n):
    sum = 0
    for i in range(1, n): # to excude the number not taking range(1, n + 1)
        if n % i == 0:
            sum += i
    if sum == n:
        print("Give number", n, "is a perfect number")
    else:
        print("Give number", n, "is not a perfect number")

n = int(input("Enter a number: "))
Perfect(n)
