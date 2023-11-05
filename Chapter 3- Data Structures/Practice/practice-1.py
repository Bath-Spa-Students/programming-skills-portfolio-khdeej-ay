# Given a Python list, write a program to remove all occurrences of item 20.
# Given list: list1 = [5, 20, 15, 20, 25, 50, 20]

# initial list 
list1 = [5, 20, 15, 20, 25, 50, 20]
# using list comprehension to remove all occurences of 20 in the list
list1 = [item for item in list1 if item != 20]
# print the list after all occurences of 20 are removed
print(list1)