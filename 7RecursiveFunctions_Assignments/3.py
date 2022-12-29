# Q.3 Write a program to reverse a given number using recursive function.

def reverse(n, reminder=0):
    if n != 0:
        reminder = (reminder+(n % 10))*10
        n //= 10
        return reverse(n, reminder)
    else:
        return reminder//10

n = int(input("Enter a number to reverse: "))
print(reverse(n))
