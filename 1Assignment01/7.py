# Convert distance given in feet and inches into meter and centimeter.
distance_feet = float(input("Distance in feet: "))
distance_inch = float(input("Distance in inches: "))
distance_meter = distance_feet * 0.3048 + distance_inch * 0.0254
distance_cm = distance_feet * 30.48 + distance_inch * 2.54
print("Distance in meter: ",distance_meter)
print("Distance in centimeter: ",distance_cm)