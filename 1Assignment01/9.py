# WAP to calculate selling price of book based on cost price and discount. 
cp = int(input("Input cost price of book: "))
dis = int(input("Input discount percentage on book: "))
dis = (dis / cp) * 100
print("Selling price of book is",cp - dis,"rupees")