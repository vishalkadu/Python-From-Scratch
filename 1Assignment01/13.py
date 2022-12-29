# Assign two number and swap it without using third variable. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("\nBefore swapping,")
print("First number ",a)
print("Second number ",b)
a, b = b, a
print("\nAfter swapping,")
print("First number ",a)
print("Second number ",b)


