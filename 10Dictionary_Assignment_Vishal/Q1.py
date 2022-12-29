# Q1. Python Program to Add a Key-Value Pair to the Dictionary
dict = dict()
n = int(input("Enter how many keys to add: "))
for i in range(n):
    print("Inset at index: ", i)
    k = input("Enter key: ")
    v = input("Enter value: ")
    dict[k] = v
print("Dictionary: ", dict)
