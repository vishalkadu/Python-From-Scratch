'''
Q.1 Write program to find sum of following series using functions :
1! + 2!  + 3! + 4! +..... + n!''
Note : For fact and sum two recursive functions 
'''
def fact(n):
    if n >= 1:
        return n * fact(n-1)
    else:
        return 1


def sum(n):
    if n >= 1:
        return fact(n) + sum(n-1)
    else:
        return 0


print('''Program to find sum of following series using functions :
1! + 2!  + 3! + 4! +..... + n!''')

n = int(input("Enter value of n: "))
print("Ans: ",sum(n))
