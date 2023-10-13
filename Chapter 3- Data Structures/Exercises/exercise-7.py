#list of places I would like to visit (not in alphabetical order)
places = ["London", "Rome", "NYC", "Berlin", "Greece", "Georgia"]

#print list in original order
print(places)

#sorting list in alphabetical order without changing the actual list
sorted_places = sorted(places)
#printing the alphabetical list
print(sorted_places)

#proving that the actual list is in the original order
print(places)

#sorting list in reverse order without changing the actual list
reversed_places = sorted(places, reverse=True)
#printing the reverse list
print(reversed_places)

#proving AGAIN that the actual list is in the original order
print(places)

#using the reverse function to reverse the list elements
places.reverse()
#printed proof that the actual list is now changed to the reversed list
print(places)

#using reverse AGAIN to revert the list back to its original order
places.reverse()
#printing the list after reversing it twice; back to the original list
print(places)

#using the sort function to sort the actual list in alphabetical order
places.sort()
#printed proof that the actual list is now changed to the alphabetical list
print(places)

#using sort AGAIN to revert the list back to its original order
places.sort()
#printing the list after sorting it twice; back to the original list
print(places)