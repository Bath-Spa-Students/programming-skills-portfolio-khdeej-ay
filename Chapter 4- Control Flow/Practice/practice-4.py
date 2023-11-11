'''Write a python program with an if-else statement that displays 'Speed is 
normal' if the speed variable is within the range of 24 to 56. If the speed 
variable's value is outside this range, display 'Speed is abnormal''' 

# user inputs speed
speed = int(input("Enter the speed: "))

# checks if speed is within 24 and 56
if speed >= 24 and speed <= 56: 
    print(f'Speed ({speed}) is normal.')
# runs if speed is outside range (more than 56 or less than 24)
else: 
    print(f'Speed ({speed}) is abnormal.')