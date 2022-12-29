# 5. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age = int(input("Input your age: "))
gender = input("Input your gender: ")

if(age >= 18 and gender =='f'): 
    print("Shehnai, get married")
elif(age >= 21 and gender =='m'): 
    print("Shehnai get married")
elif(age >= 18 and gender =='F'): 
   print("Shehnai, get married")
elif(age >= 21 and gender =='M'):
    print("Shehnai get married")
else:
    print("Go study")






'''
if (age >= 18 and gender =='f') or (age >= 21 and gender =='m'): 
    print("Marry")
elif (age >= 18 and gender =='F') or (age >= 21 and gender =='M'):
  print("Marry")
else:
    print("Don't Marry")
'''

'''
if age >=18 and (gender == 'f' or gender =='F') or age >=21 and (gender == 'M' or gender =='m') :
    print("Shehnai")
else:
    print("Don't Marry")
'''
