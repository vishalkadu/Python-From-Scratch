'''
1. Write a program to prompt user to enter userid and password. If Id and
password is incorrect give him chance to re-enter the credentials. Let him try 3
times. After that program to terminate.
'''
userid_in = 841283
password_in = '@OmSaiRam#'
for i in range(1,4):
    userid = int(input("Enter userid: "))
    password = input(("Enter password: "))
    if userid_in == userid and password_in == password:
        print("Correct credentials,bye")
        break
    else:
        print("Incorrect username or password, please re-enter your credentials\nAttempts left:",3-i)
