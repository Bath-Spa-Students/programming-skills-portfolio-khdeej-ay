'''Make several dictionaries, where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner's name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, 
print everything you know about each pet'''

# list containing several dictionaries each representing one pet's information
pets = [{"kind":"cat" , "owner":"Amna"},
        {"kind":"gerbil" , "owner":"Salma"},
        {"kind":"dog" , "owner":"Korra"},
        {"kind":"snake" , "owner":"Fionna"},
        {"kind":"sparrow" , "owner":"Zenitsu"}]

# loop to go through the list and print each pet's information
for each_pet in pets:
    # printing a new line to make the code cleaner
    print("\n")
    # printing each pet's name
    print(f"Kind of pet: {each_pet['kind']}")
    # printing each pet's owner
    print(f"Owner\'s name: {each_pet['owner']}")