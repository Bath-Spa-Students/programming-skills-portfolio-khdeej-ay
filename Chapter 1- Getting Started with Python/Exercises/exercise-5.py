# Write a Python program which accepts the radius of a circle from the user and compute the area.

print("Enter the radius:")
radius = int(input())
import math
area = radius * radius * math.pi
print("Area of circle:", area)