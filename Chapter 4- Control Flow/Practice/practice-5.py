'''Write a Python program that uses the elif statement to determine the 
season based on the month provided as input.'''

# user inputs a month
month = input("Enter the month: ").strip().title()

# checks if it is Spring
if month == "March" or month == "April" or month == "May":
    print(f'It is spring in {month}.')
# checks if it is Summer
elif month == "June" or month == "July" or month == "August":
    print(f'It is summer in {month}.')
# checks if it is Fall
elif month == "September" or month == "October" or month == "November":
    print(f'It is fall in {month}.')
# checks if it is Winter
elif month == "December" or month == "January" or month == "February": 
    print(f'It is winter in {month}.') 