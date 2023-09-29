# Exercise 3: Print date and Time :ballot_box_with_check:

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))