for i in range(1, 6):
    for j in range(1, 6-i):
        print("  ", end=" ")
    for k in range(i, i+i):
        print(k, end="  ")
    for j in range(k-1, i-1, -1):
        print(j, end="  ")
    print()
