# Q10. Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions
sample1 = 'Program to Take in Two Strings'
sample2 = 'Display the Larger String without Using Built-in Functions'
count1 = 0
count2 = 0
for i in sample1:
    count1 += 1
for i in sample2:
    count2 += 1

if count1 > count2:
    print("String1 is large")
else:
    print("String2 is large")


'''if len(sample1) > len(sample2):
    print("String1 is large")
elif len(sample2) > len(sample1):
    print("String2 is large")'''
