# Q2. Python Program to Concatenate Two Dictionaries Into One.
dict1 = {'we': 'rtt', 'io': 'po', 'yu': 'hjj'}
dict2 = {1: 'rtt', 2: 'po', 3: 'hjj'}
for i, j in dict2.items():
    dict1[i] = j
print(dict1)

'''

dict1 = {'we': 'rtt', 'io': 'po', 'yu': 'hjj'}
dict2 = {1: 'rtt', 2: 'po', 3: 'hjj'}
concat = dict1 | dict2
print(concat)

'''
