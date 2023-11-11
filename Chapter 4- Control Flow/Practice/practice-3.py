'''Write a python program with nested decision structures that perform the 
following: If amount1 is greater than 10 and amount2 is less than 100, 
display the greater of amount1 and amount2'''

# ask user to input amount1
amount1 = int(input("Enter the first amount: "))
# ask user to input amount2
amount2 = int(input("Enter the second amount: "))

# checks if amount1 is more than 10
if amount1 > 10: 
    # and checks if amount2 is less than 100
    if amount2 < 100: 
        # if top if's are true, then checks if amount1 is more than amount2
        if amount1 > amount2:
            print(f'Amount1 ({amount1}) is the greater amount.')
        # else if top if's are true, checks if amount2 is more than amount1
        elif amount1 < amount2: 
            print(f'Amount2 ({amount2}) is the greater amount.')