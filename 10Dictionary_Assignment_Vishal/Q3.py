# Q3. Python Program to Check if a Given Key Exists in a Dictionary or Not
dict1 = {'we': 'rtt', 'io': 'po', 'yu': 'hjj'}
key = input("Enter key to find: ")
for i in dict1:
    if i == key:
        print("Key:", key, "exist in dictionary")
