'''
    3. Create a class Shirt with members as sid,sname,type(formal 
    etc), price and size(small,large etc).
        Add following methods: 
            j. Constructor (Support both parameterized and parameterless) 
            k. Destructor 
            l. ShowBook 
            m. For each size of shirt price should change by 10%.
            (eg. If 1000 is price then small price = 1000, medium =1100, large=1200 and xlarge=1300) Use static concept.

'''


class Shirt:
    scnt = 100
    def __init__(self,sname='Peter', type='Formal', price=600, size='small'):
        Shirt.scnt += 1
        self.sid = Shirt.scnt
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("I'm Destructor")

    def ShowShirt(self):

        if self.size == 'Medium':
            self.price += self.price*0.1
        elif self.size == 'Large':
            self.price += self.price*0.2
        elif self.size == 'Xlarge':
            self.price += self.price*0.3
        else:
            self.price = self.price

        print("----------------------------------------")
        print(" Sid: {0} \n Sname: {1} \n Type: {2} \n Price: {3}\n Size  : {4} ".format(self.sid, self.sname, self.type, self.price, self.size))
        print("----------------------------------------")


S = Shirt()
S.ShowShirt()

S = Shirt('Armani-S', 'Informal', 1000, 'Small')
S.ShowShirt()
S = Shirt('Armani-M', 'Formal', 1000, 'Mediium')
S.ShowShirt()
S = Shirt('Armani-L', 'Casual', 1000, 'Large')
S.ShowShirt()
S = Shirt('Armani-XL', 'Party', 1000, 'Xlarge')
S.ShowShirt()

