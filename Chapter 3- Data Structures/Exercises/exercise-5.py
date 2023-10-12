#create a list of guests I would like to invite
guests = ["Maha", "Sappho", "Emily", "Anne"]

#variable to store the message of the invitation
message = "I would like to invite you to dinner.\n"

#print the invitation for each friend
print(f"{guests[0]}, {message}")     #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3

#store the message of the person who cannot make it to dinner
absent = "I am sorry you can't make it to dinner. Hope you are doing alright!"

#print the message to the person who cannot make it
print(f"\n{guests[1]}, {absent}\n")

'''modify the list at the index of the person who couldn't make it 
with the new person I am inviting'''
guests[1] = "Amna"

#print the second group of invitation messages one for each guest in the list
print(f"\n{guests[0]}, {message}")     #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3