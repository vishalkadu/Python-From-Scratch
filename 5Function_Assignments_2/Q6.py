'''
Q6. Write a program to check if given number is perfect square or not.
Hint: Perfect square formula: N = x^2
If x = 9, and N = x2. This means, N = 9^2 = 81. Here, 81 is a perfect square because it is the
square of a whole number, 9.
Note: You will need to use the library math(just like we used 'random' library) and function
'sqrt()' from this library.
Example:
import math
s = int(math.sqrt(81))
print(s)
'''
import math
def PerfectSquare(n):
    if math.sqrt(n) == int(math.sqrt(n)):  # x.0 == int(x.0) -> True
        return n
    else:
        return -1
n = int(input("Enter a number: "))
if PerfectSquare(n) != -1:
    print(n,"is a perfect square")
else:
    print(n,"is not a perfect square")