'''You have given a Python list. Write a program to find value 20 in the list, 
and if it is present, replace it with 200. Only update the first occurrence 
of an item. Work with the given list: list1 = [5, 10, 15, 20, 25, 50, 20]'''

# create given list1
list1 = [5, 10, 15, 20, 25, 50, 20]

# checks if 20 is in the list
if 20 in list1:
    # if 20 is in the list, first 20 is replaced by 200
    list1[list1.index(20)] = 200

# print the list (first 20 is replaced by 200)
print(list1)