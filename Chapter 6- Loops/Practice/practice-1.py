# Write a Python program that uses a while loop to print the even numbers from 2 to 10.

# initialize the iterator variable to 0
i = 0
# while loop to loop through the numbers
while True: 
    # augmented addition (+2 because we only need even numbers)
    i +=2
    # print is after the addition because we don't need the initial 0 to print
    print(i)
    # if statement to check if i is equal to 10
    if i == 10: 
        # loop breaks when i = 10 (after printing it)
        break