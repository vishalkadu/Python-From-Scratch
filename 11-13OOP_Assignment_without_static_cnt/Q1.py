'''
1. Create a class Book with members as bid,bname,price and 
author.
# Add following methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor 
c. ShowBook

'''


class Book:

    def __init__(self, bid= 1001,name='Let Us C', price=290, author='Yashavant Kanetkar'):
        self.bid = bid
        self.bname = name
        self.price = price
        self.author = author

    def __del__(self):
        print("Called Destructor")

    def ShowBook(self):
        print("----------------------------------------")
        print("Bid   : {0}".format(self.bid))
        print("Bname : {0}".format(self.bname))
        print("Price : {0}".format(self.price))
        print("Author: {0}".format(self.author))
        print("----------------------------------------")

B = Book()
B.ShowBook()

B = Book(1002,'Operating System Concepts', 4000, 'Peter B. Galvin')
B.ShowBook()

B = Book(1003,'Ek Hota Carver', 459, 'Vina Gavankar')
B.ShowBook()

B = Book(1004,'Man Me Hai Vishwaas', 200, 'Vishwas Nangre Patil')
B.ShowBook()

B = Book(1005,'Computer Networks', 4000, 'Andrew S. Tanenbaum')
B.ShowBook()


