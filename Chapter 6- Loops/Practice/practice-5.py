'''Write a Python program that uses a while loop to find the largest number among 
a series of user-input values until they enter '0' to exit the loop. '''

# variable max to store the largest number
max = 0
# while loop runs till break condition is met
while True: 
    # user inputs a number stored in variable num
    num = int(input("Enter a number ('0' to exit): "))
    # if statement checks if num = 0
    if num == 0: 
        # when if condition is met, loop breaks
        break
    # elif statement checks if num input is more than num stored in max
    elif num > max: 
        # if num input > num in max then max is overwritten
        max = num
    # else statement runs for every other condition (not mentioned)
    else: 
        # loop runs again when num < max (user inputs again)
        continue
# prints largest number when loop is broken
print(f"Largest number: {max}")