# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n = int(input("Enter nth value: "))
dict2 = {x: x*x for x in range(1, n+1)}
print("Dictionary: ", dict2)

'''
dic = dict()
for x in range(1,n+1):
    dic[x] = x*x
print(dic)

'''
