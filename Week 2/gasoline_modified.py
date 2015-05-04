"""
File: jayawant_gasoline.py
Author: Pallavi Jayawant
Description:
    Prompt for the number of gallons of gasoline
    convert to a float
    calculate the number of pounds of carbon dioxide produced
    calculate the barrels of crude oil required
    calculate the average cost in US dollars
    print all of this information
"""

#ask user to input number of gallons of gasoline and convert it to float if
# the user enters a valid inout

while True:
    gas_gallons = raw_input('Please enter the number of gallons of gasoline: ')
    if gas_gallons.isdigit():
        gas_gallons = float(gas_gallons)
        break
    else:
        print 'You need to enter an integer for the number of gallons of gasoline.'
        

#1 gallon of gasoline produces approximately 19.64 pounds of carbon dioxide
carbon_dioxide_pounds = gas_gallons*19.64

#output the pounds of carbon dioxide produced
print gas_gallons,'gallons of gasoline produces approximately',carbon_dioxide_pounds,'pounds of carbon dioxide.'



##while True:
##    gas_gallons = raw_input('Please enter the number of gallons of gasoline: ')
##    try:
##        gas_gallons = float(gas_gallons)
##        break
##    except ValueError:
##        print 'You need to enter an integer for the number of gallons of gasoline.'
