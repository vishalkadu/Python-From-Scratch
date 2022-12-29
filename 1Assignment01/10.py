# WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic. 
basic = int(input("Enter basic salary of employee: "))
da = int(input("Enter da percentage: "))
ta = int(input("Enter ta percentage: "))
hra = int(input("Enter hra percentage: "))
da1 = da / basic * 100
ta1 = ta / basic * 100
hra1 = hra / basic * 100
print("The total salary of employee is",basic + da1 + ta1 + hra1)

'''
da /= basic * 100
ta /=  basic * 100
hra /=  basic * 100
print("The total salary of employee is",basic + da + ta + hra)
'''
