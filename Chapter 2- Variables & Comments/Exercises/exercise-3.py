'''Exercise 3: Use a variable to represent a person’s name, and include some whitespace 
characters at the beginning and end of the name. 
Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions: 
lstrip(), rstrip(), and strip().'''

name = "   \n\tAmelia\n   "
print(name)   #print the name with added space

print(name.lstrip())    #print name removing space on left
print(name.rstrip())    #print name removing space on right
print(name.strip())     #print name removing space everywhere