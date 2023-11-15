# Write a Python program to merge two dictionaries into one.

# first dictionary (2 of my fav books)
dict_one = {
    "Seven Husbands of Evelyn Hugo" : "Taylor Jenkins",
    "One Last Stop" : "Casey McQuiston"
}
# second dictionary (2 more fav books)
dict_two = {
    "The Song of Achilles" : "Madeline Miller",
    "They Both Die at the End" : "Adam Silvera"
}
# empty dict to merge the dict_one and dict_two
books = {}
# update method adds dict_one to books
books.update(dict_one)
# update method adds dict_two to books
books.update(dict_two)
# print dict books (with dict_one and dict_two merged into it)
print(f"Favourite Books: {books}")