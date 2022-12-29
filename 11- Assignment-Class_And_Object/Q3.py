'''
3. Create a class Shirt with members as sid,sname,type(formal etc), 
price and size(small,large etc) .Add following methods:
g. Constructor (Support both parameterized and parameterless)
h. Destructor 
i. `ShowBook` > ShowShirt

'''

class Shirt:
    cnt = 100

    def __init__(self, sname='Peter', type='Formal', price=600, size='Large'):
        Shirt.cnt += 1
        self.sid = Shirt.cnt
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("I'm Destructor")

    def __str__(self):
        pass

    def ShowShirt(self):
        print("----------------------------------------")
        print(" Sid: {0} \n Sname: {1} \n Type: {2} \n Price: {3}\n Size  : {4} ".format(self.sid, self.sname, self.type, self.price, self.size))
        print("----------------------------------------")


S = Shirt()
S.ShowShirt()

S = Shirt('Armani', 'Informal', 2000, 'Small')
S.ShowShirt()

S = Shirt('Cotton Candy', 'Formal', 500, 'Large')
S.ShowShirt()