''' Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as One of my favorite books is 
Alice in Wonderland. Call the function, making sure to include a book title 
as an argument in the function call.'''

# def is used to define the favorite_book function, with fav_book as parameter
def favorite_book(fav_book):
    # prints a message about favorite book, where fav_book is the parameter
    print(f"One of my favorite books is {fav_book}.")

# calling favorite book function with my favorite book as the argument
favorite_book("Ace of Spades")