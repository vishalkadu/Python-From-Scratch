# Write a program to calculate the percentage of student based on marks of any5 subjects.

RollNo = int(input("Enter Students Roll Number: "))
Physics = int(input("Enter Marks For Physics: "))
Chemistry = int(input("Enter Marks For Chemistry: "))
Mathematics = int(input("Enter Marks For Mathematics: "))
Biology = int(input("Enter Marks For Biology: "))
PhysicalEducation = int(input("Enter Marks For Physical Education: "))

print("\n")
print("Marks For Roll Number: ", RollNo)
print("\tMarks For Physics: ", Physics)
print("\tMarks For Chemistry: ", Chemistry)
print("\tMarks For Mathematics: ", Mathematics)
print("\tMarks For Biology: ", Biology)
print("\tMarks For Physical_Education: ", PhysicalEducation)

TotalMarks = Physics + Chemistry + Mathematics + Biology + PhysicalEducation
Percentage = TotalMarks/500*100

print("Total Marks: ", TotalMarks)
print("Percentage: ", Percentage)
