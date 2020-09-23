#! python3
#
# Find the hypotenuse
# Your program will ask the user to enter in the 2 short sides of a right triangle.
# You will calculate the length of the hypotenuse and display the result.
# You will need to use the math module to use the command that finds the square root.
#
# Inputs:
# side, side
#
# Outputs:
# hypotenuse
#
# Test output
# input sides of 5 and 7 should give hypotenuse of 8.60232526704

import math

a = input("Enter one of the short sides of a right triangle ")
b = input("Enter the other short side of the right triangle ")

h = math.sqrt(float(a)**2 + float(b)**2)

print("The length of the hypotenuse is " + str(h))
