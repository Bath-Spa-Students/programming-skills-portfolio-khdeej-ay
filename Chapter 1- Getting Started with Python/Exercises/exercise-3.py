# Exercise 3: Print date and Time :ballot_box_with_check:

# imports the date and time class from datetime module
from datetime import datetime

# current variable stores the datetime object
current = datetime.now()

# prints date and time as day/month/year and hour:minute:second
print ("Current date and time:", current.strftime("%d/%m/%Y %H:%M:%S"))