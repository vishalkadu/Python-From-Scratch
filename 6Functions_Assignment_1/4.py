'''
4. Write a program to find print the following Fibonacci series using
functions:
 1 1 2 3 5 8 n terms
'''
def fibo(a, b, n):
    for i in range(1, n+1):
        c = a + b
        print(c)
        a = b
        b = c
a = 1
b = 0
n = int(input("How many numbers of series: "))
print("Fibonacii series: ")
fibo(a, b, n)

'''
def fibo_recursive(a, b, n):
    if n == 0:
        return
    else:
        c = a + b
        print(c)
    return fibo_recursive(b, c, n-1)
fibo_recursive(a, b, n)
'''