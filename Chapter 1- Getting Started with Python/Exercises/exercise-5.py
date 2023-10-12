# Write a Python program which accepts the radius of a circle from the user and compute the area.

#used a variable to store the radius inputed as an integer
radius = int(input("Enter the radius: "))

#imported the math module to get access to the pi variable
import math

#used the area of circle formula (used pi from the math module)
area = radius * radius * math.pi

#print area of circle
print("Area of circle:", area)