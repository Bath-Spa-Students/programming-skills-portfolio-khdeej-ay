#create a list of guests I would like to invite
guests = ["Maha", "Sappho", "Emily", "Anne"]

#variable to store the message of the invitation
message = "I would like to invite you to dinner."

#print the invitation for each friend
print(f"{guests[0]}, {message}")     #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3

#store the message of the person who cannot make it to dinner
absent = "I am sorry you can't make it to dinner. Hope you are doing alright!"

#print the message to the person who cannot make it at index 1
print(f"\n{guests[1]}, {absent}")

'''modify the list at the index of the person who couldn't make it 
with the new person I am inviting'''
guests[1] = "Amna"

#print the second group of invitation messages one for each guest in the list
print(f"\n{guests[0]}, {message}")     #guest 1 at index 0
print(f"{guests[1]}, {message}")     #guest 2 at index 1
print(f"{guests[2]}, {message}")     #guest 3 at index 2
print(f"{guests[3]}, {message}")     #guest 4 at index 3

#message that I can only invite two people to dinner
limit = "I have just been informed that I can only invite two people to dinner"
#print this message informing them about the guest limit being 2 people
print(f"\nTo all the guests I had invited to dinner, {limit}.")

#removing the guest at index 3: Anne
uninvite_1 = guests.pop(3)
#print an apology to Anne, the guest at index 2
print(f"\n{uninvite_1}, I am unable to keep my word of inviting you to dinner. I apologize for any inconvenience I may have caused.")

#removing the guest at index 2: Emily
uninvite_2 = guests.pop(2)
#print an apology to Emily, the guest at index 3
print(f"{uninvite_2}, I am unable to keep my word of inviting you to dinner. I apologize for any inconvenience I may have caused.")

#message to both guests that they are on the list and still invited
invited = "You are still invited to dinner. I hope to see you there."

#print invitation to guest at index 0
print(f"\nCongratulations {guests[0]}! {invited}")

#print invitation to guest at index 1
print(f"Congratulations {guests[1]}! {invited}")

#using del to delete the entire list 
del guests[: ]

#print list to make sure it is empty
print(f"\nEmpty guest list: {guests}")