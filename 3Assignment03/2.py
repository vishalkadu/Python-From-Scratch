'''
2. Enter number of students from user. For those many students accept marks of 5
subject marks from user and calculate percentage. Display all percentage and
average percentage of students.
'''
nofst = int(input("How many student's: "))
# sub = int(input("How many subject's: "))
# accept_total = int(input("Enter total marks of all suject: "))
total = 0
avg_per = 0
prev_per = 0
prev_total = 0
for j in range(1,nofst+1):
    print("Enter student",j,"marks,")
    for i in range(1,6):            #  for i in range(1,sub+1):
        print("Enter subject",i,end=" ")
        marks = int(input("marks: "))
        total += marks
    per = total/500*100             #  per = total/accept_total*100
    print("Student",j,"Total marks:",total-prev_total,"and Percentage:",per-prev_per)
    prev_per = per
    prev_total = total
avg_per += per
avg_per /= nofst
print("\n------------Average percentage of",nofst,"students:",avg_per,"---------------")

    
