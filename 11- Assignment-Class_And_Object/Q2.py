'''
2. Create a class Product with members as pid,pname,price and 
quantity .Add following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor 
f. `ShowBook` > ShowProduct

'''

class Product:
    cnt = 101
    def __init__(self,Name='Laptop Bag',Price=899,Quantity=2000):
        self.pid = Product.cnt
        self.pname = Name
        self.price = Price
        self.quantity = Quantity
        Product.cnt += 1

    def __del__(self):
        print("I'm Destructor")

    def ShowProduct(self):
        print("---------------------------------------------------")
        print("Pid      : ",self.pid)
        print("Pname    : ",self.pname)
        print("Price    : ",self.price)
        print("Quantity : ",self.quantity)
        print("---------------------------------------------------")

P = Product()
P.ShowProduct()

P = Product('Shoes',80000,1)
P.ShowProduct()

P = Product('Laptop',49000,2000)
P.ShowProduct()

P = Product('Tablet',30000,2000)
P.ShowProduct()

P = Product('Pen',10,20000)
P.ShowProduct()

