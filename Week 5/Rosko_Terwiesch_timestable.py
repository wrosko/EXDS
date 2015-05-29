"""
File: Rosko_Terwiesch_timestable.py
Authors: Wade Rosko and Mats Terwiesch
Description: User inputs some number and a starting point, program
prints a multiplication table

"""

user_number = raw_input("Please enter a number: ")
last_multiple = raw_input("Enter the maximum value of the times table:  ")
print ""

# The following two while loops ensure that the user has entered
# an integer, then converts the input to a float

while True:
    if user_number.isdigit() == False:
        print "You must enter a positive integer!"
        user_number = raw_input("Please enter a number: ")
    else:
        user_number = float(user_number)
        break
    
while True:
    if last_multiple.isdigit() == False:
        print "You must enter a positive integer!"
        last_multiple = raw_input("Enter the maximum value of the times table:  ")
    else:
        last_multiple = float(last_multiple)
        break

# While loop performs the multiplication operation, subtracts one
# until there are no more operations in the times table

while last_multiple  > 0:
    multiple = user_number * last_multiple
    print user_number, " x ", last_multiple, " is ", multiple
    last_multiple = last_multiple - 1


    
    
    
