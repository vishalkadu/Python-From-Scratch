# Q5. Python Program to Count the Number of Vowels in a String
sample = 'a cat eats mice'
cnt = 0
for i in sample:
    if i in ('aeiou') or i in ('AEIOU'):
        cnt += 1
print("Vowels count: ", cnt)
