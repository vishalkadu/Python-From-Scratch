'''
1. Create a class Book with members as bid,bname,price and 
author.
# Add following methods:
a. Constructor (Support both parameterized and parameterless)
b. Destructor 
c. ShowBook

'''


class Book:
    count = 999

    def __init__(self, name='Let Us C', price=290, author='Yashavant Kanetkar'):
        Book.count += 1
        self.bid = Book.count
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


B = Book('Operating System Concepts', 4000, 'Peter B. Galvin')
B.ShowBook()

B = Book('Ek Hota Carver', 459, 'Vina Gavankar')
B.ShowBook()

B = Book('Man Me Hai Vishwaas', 200, 'Vishwas Nangre Patil')
B.ShowBook()

B = Book('Computer Networks', 4000, 'Andrew S. Tanenbaum')
B.ShowBook()

B = Book()
B.ShowBook()
