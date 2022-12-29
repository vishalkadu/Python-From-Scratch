'''
2. Create a class Product with members as pid,pname,price and 
quantity .Add following methods:
d. Constructor (Support both parameterized and parameterless)
e. Destructor 
f. `ShowBook` > ShowProduct

'''

class Product:

    def __init__(self,Pid = 101,Name='Laptop Bag',Price=899,Quantity=2000):
        self.pid = Pid
        self.pname = Name
        self.price = Price
        self.quantity = Quantity


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

P = Product(102,'Shoes',80000,1)
P.ShowProduct()

P = Product(103,'Laptop',49000,2000)
P.ShowProduct()

P = Product(104,'Tablet',30000,2000)
P.ShowProduct()

P = Product(105,'Pen',10,20000)
P.ShowProduct()

