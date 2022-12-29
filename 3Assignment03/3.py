'''
3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.
'''
passenger = int(input("Enter number of passenger: "))  
ticket = int(input("Enter ticket price: "))
total = 0
for i in range(1, passenger+1):
    print("\nPassenger:", i)
    age = int(input("Enter person's age: "))
    if age < 12:
        total += ticket - ticket*0.3  # a. 30% discount childerns
        price = ticket - ticket*0.3
        print("Passenger", i, "ticket Rs:", price)
    elif age > 59:
        total += ticket - ticket*0.5  # b. 50% discount senior citizens
        price = ticket - ticket*0.5
        print("Passenger", i, "ticket Rs:", price)
    else:
        total += ticket               # c. pay full, no discount
        price = ticket*1
        print("Passenger", i, "ticket Rs:", price)
print("\n----------Total of tickets of",passenger, "passenger is Rs.", total, "only.--------")