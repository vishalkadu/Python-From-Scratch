# 4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged
from re import A

'''
4. Python Program to Form a New String where the First Character and
the Last Character have been Exchanged
'''
s = 'Python Program to Form a New String'
new_string = s[-1] + s[1:-1] + s[0]
print("New string:", new_string)
