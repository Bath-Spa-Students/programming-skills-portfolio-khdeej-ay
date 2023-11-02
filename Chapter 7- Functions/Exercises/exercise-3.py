'''Write a function called make_shirt() that accepts a size and the text of 
a message that should be printed on the shirt. The function should print a 
sentence summarizing the size of the shirt and the message printed on it. 
Call the function once using positional arguments to make a shirt. 
Call the function a second time using keyword arguments.'''

# def is used to define the make_shirt function, with size and text as parameters
def make_shirt(size, text): 
    # prints a message about shirt, where size and text are parameters
    print(f"The shirt size is {size} and the message printed on it is \"{text}\".")

# call function using positional arguments (size first then text later)
make_shirt("L", "You are enough just as you are")
# call function using keyword arguments (in any order)
make_shirt(text = "Someone, I tell you, in another time will remember us", size = "XL")