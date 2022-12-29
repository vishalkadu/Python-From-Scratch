'''8_a. Write a program to print the following series :
1! + 2! + 3! + 4! + …..n!
'''
print("Series 1! + 2! + 3! + 4! + .... + n!")
n = int(input("Enter n value: "))
factorial = 1
num = n
sum = 0
for i in range(1,n+1):
    factorial *= i 
    sum += factorial
print("Output:",sum)