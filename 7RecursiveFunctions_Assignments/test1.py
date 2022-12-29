#Factorial using iterative way
'''def facto(n):
    sum = 0
    fact = 1
    for i in range(1,n+1):
        fact *= i
        sum += fact
    return sum

n = 5
print(facto(n))
'''


# recursive program to count power in a number
def power(n):
    if n != 0:
        return 1 + power(n//10)
    else:
        return 0
n = 456780    
power = power(n)
print(power)

'''
Iterative way 

power = 0
while(n!=0):
    n = n//10
    power += 1
print(power)
    
'''


