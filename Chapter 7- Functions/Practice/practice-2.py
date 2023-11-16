# Write a function that calculates the factorial of a given positive integer using recursion

# define factorial function (takes only one argument)
def factorial(x):
    # if statement checks if x is 0 or 1
    if x == 0 or x == 1: 
        # when x is 0 or 1, factorial is 1 (so 1 is returned)
        return 1
    # else statement is run when x is more than 1
    else: 
        # x is multiplied by factorial(n - 1) till the if condition is met
        return x * factorial(x-1)

# prints factorial of 4 using recursion
print(f'Factorial = {factorial(4)}')