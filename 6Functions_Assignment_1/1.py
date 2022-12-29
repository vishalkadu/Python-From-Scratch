# 1. Write a program to find sum of following series using functions : 1! + 2! + 3! + 4! +….. + n!
print("Output of 1! + 2! + 3! + 4! +….. + n! series")
def factorial(num):
    fact = 1
    sum = 0
    for i in range(1,num+1): 
        fact *= i 
        sum += fact
    return sum
num = int(input("Enter the value of n: "))
print("Output: ",factorial(num))


