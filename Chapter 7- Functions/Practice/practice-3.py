# Write a Python program that uses a function to check if a given number is prime or not.

# defines function to identify if given argument is prime or not
def prime(x):
    # iterator is initialized as 1
    i = 1
    # count is initialized as 0
    count = 0
    # while loop runs until i <= x (stops when i>x)
    while i <= x:
        # checks if x is divisible by i
        if x % i == 0:
            # if true then count is incremented
            count += 1
        # i is incremented
        i += 1
    # prime numbers are divisible only by 2 numbers (1 and itself)
    if count == 2: 
        # prints that x is prime if count = 2
        print(f'{x} is a prime number.')
    # if count > 2 or count < 2 then x is not prime
    else: 
        # prints x is not a prime number because count is not 2
        print(f'{x} is not a prime number.')
# prime function takes 37 as the argument
prime(37)