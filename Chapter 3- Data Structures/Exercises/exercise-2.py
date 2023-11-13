'''Start with the list you used in Exercise 1, but instead of just
printing each person's name, print a message to them. 
The text of each message should be the same, but each message should be 
personalized with the person's name.'''

# create a list of friend names
friends = ["Hafsa", "Amna", "Siddique", "Huda"]

# same personalized message 
message = "Nice to meet you"

# print each friend's name with the message using f-strings
print(f"{message}, {friends[0]}!")     # friend at index 0
print(f"{message}, {friends[1]}!")     # friend at index 1
print(f"{message}, {friends[2]}!")     # friend at index 2
print(f"{message}, {friends[3]}!")     # friend at index 3