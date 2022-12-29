# Q5. Python Program to Sum All the Items in a Dictionary
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
sum = 0
for i, j in dic.items():
    sum += i+j
print("Sum of all the Items in a Dictionary: ", sum)
