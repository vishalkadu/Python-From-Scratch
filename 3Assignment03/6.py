# 6. Write a program to print prime numbers between 1 to 100.

n = 100
print("from 1 to", n, ",")
for i in range(2, n + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, "is a prime no")




'''
n = 100 
print("1 to",n,"prime no are following,")
for i in range(2,n+1):
        if i!=2 and i%2 ==0:
            print(end="")
            #print(i,"is not a prime no")
        elif i!=3 and i%3 == 0:
            print(end="")      
            #print(i,"is not a prime no")
        elif  i!=5 and i%5 == 0:
            print(end="")
            #print(i,"is not a prime no")
        elif i!=7 and  i%7 == 0:
            print(end="")
            #print(i,"is not a prime no")
        else:
            print(i,end=",")  
print("End")  
'''
