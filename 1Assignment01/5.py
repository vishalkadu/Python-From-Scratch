# Convert the time entered in hh,min and sec into seconds.
print("Enter current time in Hours Minutes and Seconds:")
hr = int(input("Hour: "))
min = int(input("Minutes: "))
sec = int(input("Seconds: "))
hr *= 3600 #1 hr = 60 min * 60 sec
min *= 60
sec = hr + min +sec
print("Total Seconds: ",sec)