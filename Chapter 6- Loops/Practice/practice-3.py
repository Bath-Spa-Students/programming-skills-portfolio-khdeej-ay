# Write a Python program that uses a loop to find the sum of all the numbers from 1 to 100.

# initialize the iterator variable to 0
i = 0
# initialize the sum variable to 0
sum = 0
# while loop to loop through the numbers (it runs only till i<100)
while i < 100: 
    # augmented addition (+1 because we want numbers 1-100)
    i += 1
    # each time loop iterates, i is added to sum
    sum += i
# print is outside loop because we only need one value (sum of numbers from 1 to 100)
print(f"Sum (1 to 100) = {sum}")