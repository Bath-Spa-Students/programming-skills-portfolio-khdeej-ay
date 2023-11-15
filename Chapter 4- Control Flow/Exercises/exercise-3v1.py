'''Turn your if-else chain from Exercise 4-2 into an if-elifelse chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is 
printed for the appropriate color alien.'''

# first version (alien_color is green)

# variable alien_color is green
alien_color = "green"
# checks if alien_color is green (only this block will run)
if alien_color == "green":
    # prints message if alien_color is green
    print("You have earned 5 points!")
# checks if alien_color is yellow
elif alien_color == "yellow":
    # prints message if alien_color is yellow
    print("You have earned 10 points!")
# runs when if and elif are both false
else: 
    # prints message when if and elif are false
    print("You have earned 15 points!")