'''You just heard that one of your guests can't make the dinner, 
so you need to send out a new set of invitations. You'll have to 
think of someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the 
end of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it 
with the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is 
still in your list.'''

# list of guests I would like to invite
guests = ["Maha", "Sappho", "Emily", "Anne"]

# store the general message of the invitation
message = "I would like to invite you to dinner.\n"

# print the invitation for each friend
print(f"{guests[0]}, {message}")     #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3

# store the message to the person who cannot make it to dinner
absent = "I am sorry you can't make it to dinner. Hope you are alright!"

# print the message to the person who cannot make it
print(f"\n{guests[1]}, {absent}\n")

# modifying the list at the index of the person
# who couldn't make it with the new person I am inviting
guests[1] = "Amna"

# print the second group of invitation messages one for each guest
print(f"\n{guests[0]}, {message}")   #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3