# Write a program to reverse three digit number. 

number = int(input("Enter a three digit number: ")) #e.g 123
print("Given number is",number)
digit3 = number % 10      #3
number //= 10  #12
digit2 = number % 10   #2
digit1 = number //10  #1
print("Reverse of given number is",100*digit3 + 10*digit2 + digit1) #300+20+1 = 321







'''
#for practice
#6 digit no reverse #e.g 123456
number = int(input("Enter a six digit number: ")) 
print("Given no:",number)
n6 = number % 10 #6
number //= 10 #12345
n5 = number % 10 #5
number //= 10 #1234
n4 = number % 10 #4
number //= 10 #123
n3 = number % 10 #3
number //= 10 #12
n2 = number % 10 #2
n1 = number // 10 #1

print("Reverse of given no is ",n6*100000 + n5*10000 + 1000*n4 + 100*n3 + 10*n2 + n1)

'''