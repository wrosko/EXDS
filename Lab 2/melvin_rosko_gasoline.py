"""

File: melvin_rosko_gasoline.py
Author: Andrew Melvin Wade Rosko
Description:
    Prints the pounds of carbon dioxide produced
    by a given number of gallons of gasoline
"""
#ask user to input number of gallons of gasoline 
gas_gallons = float(raw_input('Please enter the number of gallons of gasoline: ')) 
 
#1 gallon of gasoline produces approximately 19.64 pounds of carbon dioxide 
carbon_dioxide_pounds = gas_gallons*19.64 
print(carbon_dioxide_pounds)

