# dictionary named glossary that stores 10 programming keywords and their meanings
glossary = {
    "Comments" : "lines within code that will not be run or executed",
    "Dictionary" : "stores data in pairs as key:value",
    "For Loop" : "used to iterate over a sequence (list, tuple, dictinary, etc)", 
    "Function" : "a block of code that runs only when called", 
    "Elif Statement" : "used to try new condition, if previous conditions weren't true",
    "If Statements" : "structures that executes statements if the given condition is true",
    "Indentation" : "spaces that are added to the beginning of specific lines of code",
    "List" : "stores a number of items in a single variable; can  be modified", 
    "Tuple" : "stores a number of items in a single variable; cannot be modified",
    "While Loop" : "iterates and executes statements as long as a condition is true"
}
# using a for loop to access each key and it's value
for key in glossary.keys():
    # printing each key and it's value neatly with a colon and a period
    print(key + ": " + glossary[key] + ".")