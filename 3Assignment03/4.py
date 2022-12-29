'''
4. Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)
'''
n = int(input("Enter a number: "))

count = 0
ncnt = n
while ncnt != 0:
    ncnt //= 10
    count += 1  # no of digits

number = n
sum = 0
while number != 0:
    num3 = number % 10    # last digit
    sum += num3**count
    number //= 10       # reducing number or taking quotient

if n == sum:
    print(n, "is Armstrong number")
else:
    print(n, "is not an armstrong number")
