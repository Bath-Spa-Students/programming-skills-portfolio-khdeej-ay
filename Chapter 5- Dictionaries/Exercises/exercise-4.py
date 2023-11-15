'''Make a dictionary containing three major rivers and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

# dictionary to store 3 major rivers and their country
major_rivers = {
    "Nile" : "Egypt",
    "Amazon" : "Brazil",
    "Yangtze" : "China"
}
# for loop prints a sentence about each river
for key in major_rivers.keys(): 
    # 
    print("The " + key + " river runs through " + major_rivers[key] + ".") 
# print a new line to separate the outputs of each for loop
print("\n") 
# for loop prints the names (keys only) of each river in the dictionary
for key in major_rivers: 
    print(key)
# print a new line to separate the outputs of each for loop
print("\n") 
# for loop prints the name of each country (values only) mentioned in the dictionary
for key in major_rivers: 
    print(major_rivers[key])