'''Think of at least five places in the world you'd like to visit.
• Store the locations in a list. Make sure it is not in alphabetical order.
• Print your list in its original order. Don't worry about printing it neatly,
just print it as a raw Python list.
• Use sorted() to print it in alphabetical order without modifying the 
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without 
changing the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show 
that its order has changed.
• Use reverse() to change the order of your list again. Print the list to 
show it's back to its original order.
• Use sort() to change your list so it's stored in alphabetical order. 
Print the list to show that its order has been changed.
• Use sort() to change your list so it's stored in reverse alphabetical order. 
Print the list to show that its order has changed.'''

# list of places I would like to visit (not in alphabetical order)
places = ["London", "Rome", "NYC", "Berlin", "Greece", "Georgia"]

# print list in original order
print("Original order:", places)

# sort list in alphabetical order without changing the actual list
sorted_places = sorted(places)
#print the alphabetical list
print("Alphabetical order:", sorted_places)

# prove that the actual list is in the original order
print("Original order:", places)

# sort list in reverse order without changing the actual list
reversed_places = sorted(places, reverse=True)
# print the reverse list
print("Reverse order:", reversed_places)

# prove AGAIN that the actual list is in the original order
print("Original order:", places)

# use the reverse function to reverse the list elements
places.reverse()
# print proof that the actual list is now changed to the reversed list
print("Reversed list:", places)

# use reverse AGAIN to revert the list back to its original order
places.reverse()
# print the list after reversing it twice; back to the original list
print("Original list:", places)

# use the sort function to sort the actual list in alphabetical order
places.sort()
# print proof that the actual list is now changed to the alphabetical list
print("Alphabetical list:", places)

# use sort AGAIN to revert the list back to its original order
places.sort()
# print the list after sorting it twice; back to the original list
print("Original list:", places)