# Find a quote from a famous person you admire. Print the quote and the name of its author. 

#first way: used escape characters: \" to print the quotation marks
print("Sappho once said, \"When anger spreads through the breath, guard thy tongue from barking idly\". ")

#second way: added a new line then used two variable to store the quote
author = "\nEmily Dickinson once said, "
quote = '"Forever is composed of nows"' 
#print quote using f string
print(f'{author}{quote}')