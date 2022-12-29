''' 3. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message
otherwise failed. (Something like captcha) '''
import random
userid = 12911
password = '#1234@#Ui'
x = int(input("Enter userid: "))
y = input("Enter password: ")
if x == userid and y == password:
    print("Correct username and password")
    ran = random.randint(1000,9999)
    print("Input this number: ",ran)
    in_ran = int(input("type input: "))
    if ran == in_ran:
        print("Captcha verified")
    else:
        print("Captcha verification failed")
else:
    print("Incorrect username or password")