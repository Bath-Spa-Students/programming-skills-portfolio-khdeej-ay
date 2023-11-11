'''Write a python program with if statement that assigns 20 to the variable 
y and assigns 40 to the variable z if the variable & is greater than 100.''' 

# ask user to input a integer in var / can also just give var a value 
var = int(input("Enter an integer: "))

# if statement checks if var is more than 100
if var > 100:
    x = 40
    y = 20
    print(f'The value of x is {x} and y is {y}.')

# no else statement because question does not specify it