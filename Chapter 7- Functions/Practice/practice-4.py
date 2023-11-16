'''Write a Python program that defines a function to calculate the area of 
a circle, and then calls that function with a given radius.'''

# imports math module that contains exact value for pi
import math 

# defines function that calculates area of function (takes radius as argument)
def circle(radius):
    # calulates area
    area = math.pi * radius ** 2
    # returns area of circle
    return area

# prints the area of a circle of radius 4 (through the function 'circle)
print(f'Area of circle (radius = 4): {circle(4)}')