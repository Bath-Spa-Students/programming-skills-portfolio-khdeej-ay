''' Assume the lists numbers1 has 100 elements and numbers2 is an empty list. 
Write code that copies the values in numbers to numbers2. '''

# Assuming numbers1 has 100 elements
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numbers2 is an empty list
numbers2 = []

# for loop iterates through each item in the list
for number in numbers1:
    # append adds each item from numbers1 to numbers2
    numbers2.append(number)
# print list numbers2
print(numbers2)