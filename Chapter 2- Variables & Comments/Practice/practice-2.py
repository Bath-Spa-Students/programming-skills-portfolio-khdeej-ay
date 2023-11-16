'''Write a python program that takes marks as input then calculates avg 
of all courses. After calculating average, calculate the percentage of a 
student using total marks. Assume the total of all the courses marks is 
500 or take the total marks from the user as input. '''

# user inputs 5 course marks
mark1 = int(input("Marks for Course 1: "))
mark2 = int(input("Marks for Course 2: "))
mark3 = int(input("Marks for Course 3: "))
mark4 = int(input("Marks for Course 4: "))
mark5 = int(input("Marks for Course 5: "))
# calculate the total course mark by adding them
total = mark1 + mark2 + mark3 + mark4 + mark5
# print the total course mark
print(f"Total: {total}")
# calculate average by dividing total with number of courses
average = total / 5
# print average mark
print(f"Average: {average}")
# calculate percentage by *100 (same as average mark)
percentage = total / 500 * 100 
# print the percentage mark
print(f"Percentage: {percentage}")