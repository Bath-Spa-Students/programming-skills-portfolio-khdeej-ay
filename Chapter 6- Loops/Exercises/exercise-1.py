'''Write a loop that prompts the user to enter a series of pizza toppings 
until they enter a 'quit' value. As they enter each topping,
print a message saying you will add that topping to their pizza.'''

# this will runs an infinite loop unless the condition is met
while True: 
    # this question prompts the user to enter a topping to type quit to finish adding toppings
    pizza_topping = input("What pizza topping would you like (Enter 'quit' to finish)? ")
    # checks if the user entered quit (removes spaces and in lowercase ONLY!)
    if pizza_topping.strip() == 'quit':
        # if the user entered quit, the loop breaks
        break
    # if user doesn't enter quit, this code block will run
    else:
        # this message will be printed (about the topping)
        print(f'I will add {pizza_topping} to your pizza.')