# 2. Write a program to check if user has entered correct userid and password.
userid = 123456
password = '#1234@#Ui'
x = int(input("Enter userid: "))
y = input("Enter password: ")
if x == userid:
    if y == password:
        print("Correct username and password")
else:
    print("Incorrect username or password")
