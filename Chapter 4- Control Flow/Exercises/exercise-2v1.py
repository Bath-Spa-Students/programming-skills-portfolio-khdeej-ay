'''Choose a color for an alien as you did in Exercise 5-3, and write an 
if-else chain.
• If the alien's color is green, print a statement that the player just 
earned 5 points for shooting the alien.
• If the alien's color isn't green, print a statement that the player just 
earned 10 points.
•Write one version of this program that runs the if block and another that 
runs the else block.'''

# first version (runs the if block)

# variable alien_color contains element green
alien_color = "green"
# if statement checks whether the color is green
if alien_color == "green":
    #prints if the condition is true (when color is green)
    print("You have earned 5 points!")
# else statement runs when the if statement is false (color is not green)
else: 
    # prints if the condition is false (when color is not green)
    print("You have earned 10 points!")