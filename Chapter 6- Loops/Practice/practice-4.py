# Write a Python program that uses the break statement to exit a for loop when a specific condition is met. 

# list of my favourite numbers
fav_num = [6, 3, 2, 7, 12]
# for loop to iterate through each item in the list
for i in fav_num: 
    # if statement checks when i = 7
    if i == 7: 
        # loop breaks when i = 7
        break
    # prints items in list before 7
    print(i)