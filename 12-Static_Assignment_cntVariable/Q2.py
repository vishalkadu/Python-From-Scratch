'''
    2. Create a class Product with members as pid,pname,price and 
    quantity.
        Add following methods: 
            e. Constructor (Support both parameterized and parameterless) 
            f. Destructor 
            g. ShowBook 
            h. Add static member discount. 
            i. Provide methods for applying discount on price of product.

'''


class Product:

    def __init__(self, Pid=100, Name='Laptop Bag', Price=899, Quantity=2000):
        self.pid = Pid
        self.pname = Name
        self.price = Price
        self.quantity = Quantity

    def __del__(self):
        print("I'm Destructor")

    def ShowProduct(self):
        print("---------------------------------------------------")
        print("Pid      : ", self.pid)
        print("Pname    : ", self.pname)
        print("Price    : ", self.price)
        print("Quantity : ", self.quantity)
        print("---------------------------------------------------")

    def Discount(self):
        print("----------------------***-----------------------------")
        self.price -= self.price*0.1
        print("Special 10% Discounted Price for",self.pname,"is",self.price)
        print("---------------------***------------------------------")


P = Product()
P.ShowProduct()

P = Product(101,'Shoes', 80000, 1)
P.ShowProduct()
P.Discount()

P = Product(102,'Laptop', 49000, 2000)
P.ShowProduct()

P = Product(103,'Tablet', 30000, 2000)
P.ShowProduct()
P.Discount()

P = Product(104,'Pen', 10, 20000)
P.ShowProduct()
