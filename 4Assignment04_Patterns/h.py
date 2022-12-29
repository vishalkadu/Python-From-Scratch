n = 7
for i in range(1, 6):
    num = 1
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    for j in range(1, n+1):
        print(" ", end=" ")
    n -= 2
    num -= 1
    for j in range(1, i+1):
        if(i == 5 and j == 1):
            print("", end="")
        else:
            print(num, end=" ")
        num -= 1
    print()
