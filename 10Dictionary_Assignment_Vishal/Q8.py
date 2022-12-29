# Q8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

sample = 'Python Program to Count the Frequency of words words Python Program to Count the Frequency of words words'
dic = {}
for i in sample.split():
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print("Dictionary Containg Frequency of Words Appearing in a String,\n", dic)







'''for i in sample.split():
    dic[i] = sample.count(i) # we need to count the occurances of elements in 'sample'
print(dic)'''


'''
# Q. characters and their count in dictionary
sample = 'hiiihowwwwareeeeyoooou'
uni_sample = set(sample) 
dic = dict()
for i in uni_sample:
    dic[i] = sample.count(i)
print(dic)
'''
