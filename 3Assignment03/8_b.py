'''8_b. Write a program to print the following series :
N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)
'''
print("Series N + N^2 + N^3+N^4 …..+N^N (here ^ means exponent)")
num = int(input("Enter number N: "))
exp = int(input("Enter exponent ^: "))
sum = 0
for i in range(1,exp+1):
    numexp = num**i
    sum += numexp
print("Output:\t",sum)