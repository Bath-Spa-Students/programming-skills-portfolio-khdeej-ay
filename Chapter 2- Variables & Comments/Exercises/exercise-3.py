'''Exercise 3: Use a variable to represent a person's name, and include some 
whitespace  characters at the beginning and end of the name. 
Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions: 
lstrip(), rstrip(), and strip().'''

# variable name stores the person's name with some whitespace
name = "   \n\tAmelia\n   "
# prints the name with the added whitespace space
print(name)  

print(name.lstrip())    #prints name by removing space on left
print(name.rstrip())    #prints name by removing space on right
print(name.strip())     #prints name by removing space both left and right