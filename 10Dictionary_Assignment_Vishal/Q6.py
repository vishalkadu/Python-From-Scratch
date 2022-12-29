# Q6. Python Program to Multiply All the Items in a Dictionary
dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
dic = {1: 2, 3: 4}
prod = 1
for i, j in dic.items():
    prod *= i*j
print("Product of all the Items in a Dictionary: ", prod)
