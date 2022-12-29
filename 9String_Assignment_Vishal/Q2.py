# Q2. Python Program to Remove the nth Index Character from a Non-Empty String
sample = 'Sample string now remove nth index character'
print("Given String: ", sample)
ind = int(input("Enter index of element to remove: "))
sample_r = str()
for i in range(0, len(sample)):
    if i != ind:
        sample_r += sample[i]
print(sample_r)
