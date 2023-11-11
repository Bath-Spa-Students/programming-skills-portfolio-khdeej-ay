# Write a Python program which accepts the radius of a circle from the user and compute the area.

# variable stores the user's radius input as an integer
radius = int(input("Enter the radius: "))

# imports the math module to get access to the pi variable
# can also directly use the value 3.142
import math

# area of circle formula (use pi from the math module / 3.142)
area = radius * radius * math.pi

# prints area of circle
print("Area of circle:", area)