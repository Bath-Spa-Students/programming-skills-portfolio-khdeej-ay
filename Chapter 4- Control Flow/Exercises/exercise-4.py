#take user's age as an input
age = int(input("Enter your age: "))
#check if user is a baby
if age<2:
    print("You are a baby!")
#check if user is a toddler
elif age>=2 and age<4:
    print("You are a toddler!")
#check if user is a kid
elif age>=4 and age<13:
    print("You are a kid!")
#check if user is a teenager
elif age>=13 and age<20:
    print("You are a teenager!")
#check if user is an adult
elif age>=20 and age<65:
    print("You are an adult!")
#when all if and elif conditions are false, user is an elder
else: 
    print("You are an elder!")