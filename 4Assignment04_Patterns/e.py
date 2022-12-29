for i in range(1, 5):
    for k in range(1, 8-i):
        print("", end="  ")
    for j in range(1, i+1):
        if i == 1 or j == 1 or i == 5 or j == i:
            print(j, end="  ")
        else:
            print(" ", end="   ")
    print()
for i  in range(1,6):
    print("  ",i,end="")

