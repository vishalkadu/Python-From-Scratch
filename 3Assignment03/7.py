# 7. Write a program to print first 50 prime numbers.
n = 300
count = 0

print("First 50 prime no are following,")
for i in range(2, n + 1):
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i,end=",") 
            count = count + 1 
            print("is prime number no ",count)
            if count >= 50:
                break










'''
n = 300
count = 0
print("1 to",n,"prime no are following,")
for i in range(2,n+1):
    if i!=2 and i%2 ==0:
        print(end="")
    elif i!=3 and i%3 == 0:
        print(end="")      
    elif  i!=5 and i%5 == 0:
        print(end="")
    elif i!=7 and  i%7 == 0:
        print(end="")
    else:
        print(i,end=",") 
        count = count + 1 
        print("is prime number no ",count)
        if count >= 50:
            break
print("End")  


'''