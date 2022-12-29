# Q1. Python Program to Replace all Occurrences of ‘a’ with $ in a String
print("Python Program to Replace all Occurrences of ‘a’ with $ in a String")

sample = 'hi! how are you? have a nice day.'
#sample = sample.replace('a','$')
print("Given String: ", sample)
sample_r = ''
for i in sample:
    if i != 'a':
        sample_r += i
    else:
        sample_r += '$'
print("Result: ", sample_r)
