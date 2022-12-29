'''
5. Write a program to accept an integer amount from user and tell minimum
number of notes needed for representing that amount. (Use looping to optimise
the problem)
'''
amount = int(input("Enter the amount of money: "))
note2k = 2000
note500 = 500
note200 = 200
note100 = 100
note50 = 50
note10 = 10
note5 = 5
note1 = 1
tcount = 0
for i in note2k, note500, note200, note100, note50, note10, note5, note1:
    notecnt = amount//i
    print("Note Rs.", i, ",", "\n\t note needed: ", notecnt)
    amount %= i
    if notecnt >= 1:
        tcount += notecnt
print("\nTotal notes required: ", tcount)