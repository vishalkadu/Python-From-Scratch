# 9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String
#sample = 'Characters Present in a String'
sample = ''
cnt = 0
wordcnt = 1
print("Character count: ", len(sample))
for i in sample:
    cnt += 1
    if i in (' ', ',', '.'):
        wordcnt += 1
print("No of characters: ", cnt)
if cnt > 0:
    print("No of words:", wordcnt)
else:
    print("String is empty")

#print("Words count: ",len(sample.split(" ")))
