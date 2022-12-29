# Print 1 to 100 in snakes and ladder pattern.
'''
1 2 3 4 5 6 7 8 9 10 
20 19 18 17 16 15 14 13 12 11 
21 22 23
.
.
.
.
.
.
.
100 99 98 97 96 95 94 93 92 91
'''
for i in range(0,11): 
    n = i * 10 
    data = []
    for j in range(0,10):
        if n > 0:
            data.append(n-j)
    if i%2 != 0:
        data.reverse()
    for n in data:
            print(n,end=" ")
    print()