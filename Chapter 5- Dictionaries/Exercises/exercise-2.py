# dictionary named glossary that stores 5 programming keywords and their meanings
glossary = {
    "Comments" : "the lines within our code that will not be run",
    "If Statements" : "structures that executes statements if the condition is true",
    "Indentation" : "the spaces that are added to the beginning of specific lines of code",
    "List" : "stores a number of items in a single variable; can  be modified", 
    "Tuple" : "stores a number of items in a single variable; cannot be modified"
}
# printing each word(key) and it's meaning(value) neatly with a colon and a period
print([key for key in glossary.keys()][0] + ": " + glossary["Comments"] + ".")
print([key for key in glossary.keys()][1] + ": " + glossary["If Statements"] + ".")
print([key for key in glossary.keys()][2] + ": " + glossary["Indentation"] + ".")
print([key for key in glossary.keys()][3] + ": " + glossary["List"] + ".")
print([key for key in glossary.keys()][4] + ": " + glossary["Tuple"] + ".")