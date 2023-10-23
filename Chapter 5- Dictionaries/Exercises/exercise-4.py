# dictionary to store 3 major rivers and their country
major_rivers = {
    "Nile" : "Egypt",
    "Amazon" : "Brazil",
    "Yangtze" : "China"
}
# loop to print a sentence about each river
for key, value in major_rivers.items(): 
    print("The " + key + " river runs through " + value + ".") 
print("\n") #new line to separate the outputs of each loop
# loop to print names of each river in dictionary
for key in major_rivers: 
    print(key)
print("\n") #new line to separate the outputs of each loop
# loop to print name of each country mentioned in dictionary
for value in major_rivers: 
    print(major_rivers[value])
