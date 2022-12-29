'''
2.  Write a program to check if given number is Armstrong or not 
using iterative way.
'''
n = 407
power = len(str(n))
sum = 0
while(n!=0):
    rem = n%10
    n = n//10
    sum += rem ** power
print(sum)