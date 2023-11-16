# Write a Python function that takes two numbers as arguments and returns their sum.

# def is used to define the add function (takes 2 variables as parameters)
def add(x, y):
    # variable sum stores the sum of x and y
    sum = x + y
    # function returns the value of sum
    return sum

# stores the first number the user inputs
a = int(input("Enter a number: "))
# stores the second number the user inputs
b = int(input("Enter a number: "))
# print statement is used to return the sum (a and b are arguments inside add())
print(f'Sum = {add(a, b)}')