'''
Q4. Write a program to check to print all perfect numbers in the given range.
 Note: Accept the Start range and End range value from user.
'''

def PerfectNoRange(start, end):
    while(start != end):
        sum = 0
        for i in range(1, start):  # to excude the number not taking range(1, start + 1)
            if start % i == 0:
                sum += i
        if sum == start:
            print(start, end=" ")
        start += 1


start = int(input("Enter the start number: "))  # e.g. 1
end = int(input("Enter the end number: "))  # e.g. 10000
PerfectNoRange(start, end)
