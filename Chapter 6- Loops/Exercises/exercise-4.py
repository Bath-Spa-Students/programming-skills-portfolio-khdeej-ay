'''Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. Loop through the list of sandwich 
orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. After all the 
sandwiches have been made, print a message listing each sandwich that was made.'''

# list of sandwich orders
sandwich_orders = ["grilled cheese", "chicken", "egg", "club", "cheese steak"]
# empty list for finished sandwiches
finished_sandwiches = []

# loop through sandwich_orders list
for order in sandwich_orders: 
    # print a message for each sandwich
    print(f"I will make a {order} sandwich.")
    # add each sandwich made to finished_sandwiches using append()
    finished_sandwiches.append(order)

# print the finished_sandwiches list
print("\nFinished Sandwiches: ")
# loop to print list of finished sandwiches
for sandwich in finished_sandwiches:
    print(f'I made a {sandwich}.')