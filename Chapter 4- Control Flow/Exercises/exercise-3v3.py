#first version (alien_color is red)

#variable alien_color is red
alien_color = "red"
#checks if alien_color is green
if alien_color == "green":
    #prints message if alien_color is green
    print("You have earned 5 points!")
#checks if alien_color is yellow
elif alien_color == "yellow":
    #prints message if alien_color is yellow
    print("You have earned 10 points!")
#runs when if and elif are both false (not green or yellow)
else: 
    #prints message when if and elif are false (not green or yellow)
    print("You have earned 15 points!")