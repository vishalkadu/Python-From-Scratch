# If there are 20 students who like football, 30 students like badminton and 10 like both
# There are 20 who are not interested in any of the games. How many total number of students are there? 

football = 20
badminton = 30
footbad = 10
no_footbad = 20
total = football + badminton - footbad + no_footbad
print("There are total",total,"students")

#Input from user
football = int(input("Enter number of students who like football: ")) 
badminton = int(input("Enter number of students who like badminton: "))
footbad = int(input("Enter number of students who like footaball and badminton: "))
no_footbad = int(input("Enter number of students who don't like any football and badminton: "))
total = football + badminton - footbad + no_footbad
print("There are total",total,"students")