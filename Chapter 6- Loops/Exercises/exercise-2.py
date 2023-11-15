'''A movie theater charges different ticket prices depending on a person's age. 
If a person is under the age of 3, the ticket is free; if they are between 3 
and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of 
their movie ticket'''

# loop runs until break condition is met
while True: 
    # input age + convert it to integer
    age = int(input("Enter age: "))
    # if age is 0 years then loop is broken
    if age == 0: 
        break
    # if age is less than 3, ticket is free
    elif age < 3: 
        print("Ticket is free!")
    # if age is between 3 and 12, ticket is 10$
    elif age >= 3 and age < 12: 
        print("Ticket is $10.")
    # if age is above 12, ticket is 15$
    elif age >= 12: 
        print("Ticket is $15.")
    # prints new line after each loop runs
    print("\n")