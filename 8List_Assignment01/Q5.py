'''5. Python Program to Sort a List According to the Length of the 
Elements within the list.'''

data = ['wgvdbbxjnns','hi','hello','how','areyou','calm56','hind','mindnpma']
for i in range(1,len(data)):
    for i in range(0,len(data)-1) :
        if len(data[i]) > len(data[i+1]):
            data[i],data[i+1] = data[i+1],data[i]
print(data)
        