'''Write a loop that prompts the user to enter a series of pizza toppings 
until they enter a 'quit' value. As they enter each topping,
print a message saying you will add that topping to their pizza.'''

# loop keeps running unless the condition for break is met ('quit')
while True: 
    # prompts user to enter a topping and to type quit to finish adding toppings
    topping = input("What pizza topping would you like ('quit' to finish)? ").strip()
    # checks if the user entered quit
    if topping == 'quit':
        # if the user enters quit, the loop breaks
        break
    # else (no quit) this code block will run
    else:
        # prints message about the pizza topping
        print(f'I will add {topping} to your pizza.')