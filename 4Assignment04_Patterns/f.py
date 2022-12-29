for i in range(1,6):
    for j in range(i, 6):
        if i == 1 or j == 5 or j == 1 or j == i:
            print(j, end="  ")
        else:
            print(" ", end="   ")
    print()

