'''Write a python program that takes courses marks as input and then calculates 
average of all the courses. After calculating the average, calculate the 
percentage of a student using total marks. Assume the total of all the courses 
marks is 500 or take the total marks from the user as input. '''

mark1 = int(input("Marks for Course 1: "))
mark2 = int(input("Marks for Course 2: "))
mark3 = int(input("Marks for Course 3: "))
mark4 = int(input("Marks for Course 4: "))
mark5 = int(input("Marks for Course 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
print(f"Total: {total}")
average = total / 5
print(f"Average: {average}")
percentage = total / 500 * 100 
print(f"Percentage: {percentage}")