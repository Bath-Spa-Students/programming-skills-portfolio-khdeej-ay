'''A Python dictionary can be used to model an actual dictionary. However, to avoid 
confusion, let's call it a glossary.
* Think of five programming words you've learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word 
followed by a colon and then its meaning, or print the word on one line and then print 
its meaning indented on a second line. Use the newline character (\n) to insert a blank 
line between each word-meaning pair in your output.'''

# dictionary named glossary that stores 5 programming keywords and their meanings
glossary = {
    "Comments" : "the lines within our code that will not be run",
    "If statements" : "structures that executes statements if the condition is true",
    "Indentation" : "the spaces that are added to the beginning of specific lines of code",
    "Lists" : "store a number of items in a single variable; can  be modified", 
    "Tuples" : "store a number of items in a single variable; cannot be modified"
}
# print each word(key) and it's meaning(value) neatly with a colon and a period
print("Comments" + ": " + glossary["Comments"] + ".")
print("If statements" + ": " + glossary["If statements"] + ".")
print("Indentation" + ": " + glossary["Indentation"] + ".")
print("Lists" + ": " + glossary["Lists"] + ".")
print("Tuples" + ": " + glossary["Tuples"] + ".")