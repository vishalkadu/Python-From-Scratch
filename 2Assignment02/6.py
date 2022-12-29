''' 6. Accept age of five people and also per person ticket amount and then calculate total
    amount to ticket to travel for all of them based on following condition :
    a. Children below 12 = 30% discount
    b. Senior citizen (above 59) = 50% discount
    c. Others need to pay full. '''

ticket = int(input("Enter ticket price: "))
people = int(input("Enter number of people: "))  # e.g. people = 5
total = 0
for i in range(1, people+1):
    print("Person:", i)
    age = int(input("Enter person's age: "))
    if age <= 12:
        total += ticket - ticket*0.3  # a. 30% discount childerns
        price = ticket - ticket*0.3
        print("Person", i, "ticket Rs:", price)
    elif age >= 59:
        total += ticket - ticket*0.5  # b. 50% discount senior citizens
        price = ticket - ticket*0.5
        print("Person", i, "ticket Rs:", price)
    else:
        total += ticket               # c. pay full, no discount
        price = ticket*1
        print("Person", i, "ticket Rs:", price)
print("Total Rs:", total, "\nTotal of tickets of",people, "people is Rs.", total, "only.")
