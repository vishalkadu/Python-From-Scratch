'''
    1. Create a class Book with members as bid,bname,price and 
    author.
        Add following methods: 
            a. Constructor (Support both parameterized and parameterless) 
            b. Destructor 
            c. ShowBook 
            d. Add static variable count and also maintain count of objects 
            created.
            
'''


class Book:
    cnt = 100
    obj_cnt = 0
    def __init__(self, name='Let Us C', price=290, author='Yashavant Kanetkar'):
        Book.cnt += 1
        Book.obj_cnt += 1
        self.obj_cnt = Book.obj_cnt
        self.bid = Book.cnt
        self.bname = name
        self.price = price
        self.author = author

    def __del__(self):
        print("I'm Destructor")


    def ShowBook(self):
        print("----------------------------------------")
        print("Bid   : {0}".format(self.bid))
        print("Bname : {0}".format(self.bname))
        print("Price : {0}".format(self.price))
        print("Author: {0}".format(self.author))
        print("----------------------------------------")
    
    def ObjectCount(self):
        print("Object Created ",self.obj_cnt,"times.")

B = Book()
B.ShowBook()

B = Book('Computer Networks', 4000, 'Andrew S. Tanenbaum')
B.ShowBook()
B.ObjectCount()

B = Book('Operating System Concepts', 4000, 'Peter B. Galvin')
B.ShowBook()
B.ObjectCount()

B = Book('Ek Hota Carver', 459, 'Vina Gavankar')
B.ShowBook()
B.ObjectCount()

B = Book('Man Me Hai Vishwaas', 200, 'Vishwas Nangre Patil')
B.ShowBook()
B.ObjectCount()