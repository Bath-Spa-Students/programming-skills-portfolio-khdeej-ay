'''Write a Python program that uses the elif statement to determine the 
season based on the month provided as input.'''

# user inputs a month
month = input("Enter the month: ").strip().title()

if month == "March" or "April" or "May":
    print(f'It is spring in {month}.')
elif month == "June" or "July" or "August":
    print(f'It is summer in {month}.')
elif month == "September" or "October" or "November":
    print(f'It is fall in {month}.')
elif month == "December" or "January" or "February": 
    print(f'It is winter in {month}.')