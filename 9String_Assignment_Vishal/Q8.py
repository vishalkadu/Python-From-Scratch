# Q8. Python Program to Remove the Characters of Odd Index Values in a String
sample = 'String'
sample_r = str()
for i in range(0, len(sample), 2):
    sample_r += sample[i]
print(sample_r)
