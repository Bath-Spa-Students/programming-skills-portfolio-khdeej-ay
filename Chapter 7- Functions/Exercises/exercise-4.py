'''Modify the make_shirt() function so that shirts are large by default with 
a message that reads I love Python. Make a large shirt and a medium shirt with 
the default message, and a shirt of any size with a different message.'''

# def is used to define the make_shirt function, with size and text as parameters
def make_shirt(size = "Large", text = "I love Python"): 
    # prints a message about shirt, where size and text are parameters
    print(f"The shirt size is {size} and the message printed on it is \"{text}\".")

# prints default size and message
make_shirt()
# prints default message with size medium
make_shirt(size="Medium")
# prints shirt with different message and size
make_shirt("Extra-Large", "I know not what to do, my mind is divided")