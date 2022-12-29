# 3. Python Program to Detect if Two Strings are Anagrams
string1 = 'vishalay26t**ghdbx'
string2 = '26t**ghdbxshivalay'
count = [0 for x in range(26)]
for i in string1:
    count[ord(i) % 26] += 1
for i in string2:
    count[ord(i) % 26] -= 1
# print(count)
for i in count:
    if i != 0:
        print("Not Anagram")
        exit()
print("Anagram")


'''
#OR
string1 = 'vishalay'
string2 = 'shivalay'
if len(string1) == len(string2):
        if set(string1) == set(string2):
                print("This strings are anagrams")
else:
        print("This strings are not anagrams")'''

'''
#OR

string1 = 'vishalay'
string2 = 'shivalay'

ht = dict()

for i in string1:
        ht[ord(i)] = ht.get(ord(i), 0)+1

for i in string2:
        ht[ord(i)] = ht.get(ord(i), 0)-1

if sum(ht.values()) == 0:
        print("Anagram")
        exit()
print("Not Anagram")



'''
