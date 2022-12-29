'''
2.  Write a program to check if given number is Armstrong or not 
using recursive function.
'''
def armstrong(n):
    sums = 0
    if (n != 0):
        sums += (n % 10) ** power
        sums += armstrong(n//10)
    return sums


def power(n):
    if n != 0:
        return 1 + power(n//10)
    else:
        return 0


n = int(input("Enter a number: "))
power = power(n)

if n == armstrong(n):
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")