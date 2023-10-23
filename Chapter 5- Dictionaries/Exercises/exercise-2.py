# dictionary named glossary that stores 5 programming keywords and their meanings
glossary = {
    "Comments" : "lines within code that will not be run or executed",
    "If Statements" : "statement that executes statements if the given condition is true",
    "Indentation" : "spaces that are added to the beginning of specific lines of code",
    "List" : "stores a number of items in a single variable; can  be modified", 
    "Tuple" : "stores a number of items in a single variable; cannot be modified"
}
# using a for loop to access each key and it's value
for key in glossary.keys():
    #printing each key with it's value neatly separated by a colon and ending with a full stop
    print(key + ": " + glossary[key] + ".")