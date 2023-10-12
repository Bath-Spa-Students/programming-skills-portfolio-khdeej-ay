# A girl wants to buy USBs for £50. They are £6 each.
# Write a programme that calculates how many USBs she can buy and how many pounds she will have left.

#total money the girl has
total_cash = 50

#cost of one usb
one_usb = 6

#used integer division to get the maximum number of usbs she can buy
max_usb = 50 // 6

#used remainder operator to get the change left
change = 50 % 6

#print both values using f-strings
print(f"Total USB sticks she can buy: {max_usb}")
print(f"Pounds she has left: {change}")