# Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
# (Hint – Consider 450 -> 4*100 + 50*1 -> 2 : 5 notes)

amount = int(input("Enter amount : "))
note2000 = amount // 2000
note500 = amount % 2000
note500 = note500 // 500
note200 = amount % 500
note200 = note200 // 200
note100 = amount % 200
note100 = note100 // 100
note50 = amount % 100
note50 = note50 // 50
note20 = amount % 50
note20 = note20 // 20
note10 = amount % 20  # 
note10 = note10 // 10
note5 = amount % 10
note5 = note5 // 5

print("Rs 2000 Notes: ",note2000)
print("Rs 500 Notes : ",note500)
print("Rs 200 Notes : ",note200)
print("Rs 100 Notes : ",note100)
print("Rs 50 Notes  : ",note50)
print("Rs 20 Notes  : ",note20)
print("Rs 10 Notes  : ",note10)
print("Rs 05 Notes  : ",note5)

total_notes = note2000 + note500 + note200 + note100 + note50 + note20 + note10 + note5
print("Total notes  : ",total_notes)