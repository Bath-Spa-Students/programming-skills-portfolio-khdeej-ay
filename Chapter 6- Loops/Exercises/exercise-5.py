'''Using the list sandwich_orders from Exercise 6-4, make sure the sandwich 
'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the 
deli has run out of pastrami, and then use a while loop to remove all 
occurrences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandwiches.''' 

# list of sandwich orders
sandwich_orders = ["grilled cheese", "chicken", "pastrami", 
                   "egg", "pastrami", "club", "pastrami", "cheese steak"]
# empty list for finished sandwiches
finished_sandwiches = []

# message stating that deli is finished
print("The deli has run out of pastrami. \n")

# while loop to remove all orders of pastrami from sandwich orders
while "pastrami" in sandwich_orders: 
    sandwich_orders.remove("pastrami")

# loop through sandwich_orders
for order in sandwich_orders: 
    # print a message for each sandwich
    print(f"I made a {order}.")
    # add each sandwich made to finished_sandwiches
    finished_sandwiches.append(order)

# print the finished_sandwiches list
print("\nFinished Sandwiches: ")
# loop to print list of finished sandwiches
for sandwich in finished_sandwiches:
    print(sandwich)