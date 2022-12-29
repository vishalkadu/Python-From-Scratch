# 2. Sum of all odd numbers between 1 to n
def odd(n):
    sum = 0
    for i in range(2,n): #between 1 to n, hence 2 to n-1
        if i % 2 != 0:
            sum += i
    return sum
n = int(input("Enter value of n: "))
print("Sum of odd numbers between 1 to",n,"is",odd(n))


