''' Ask user if they are a natural born citizen. If they are continue,
if not print that they are ineligible.
Ask user for age, if they are >= 35 years of age continue, if not print
that they are ineligible.
Ask user for residency time. If they have lived in US for more than 14
years print that they are eligible. If they have not print that
they are ineligible.
'''
import time #imports time package for to allow for waiting between
            #certain actions
restart = False
answeredCitizenship = False
answeredAge = False
answeredResidency = False
stillEligible = True
while True:
    while not(answeredCitizenship) and stillEligible:
        citizen = raw_input('Are you a natural born citizen, yes(y) or no(n)?    ').lower()#makes input all lowercase
        if citizen.isalpha() and citizen in ['yes','y']: #if entry is yes or y
            answeredCitizenship = True
        elif not(citizen.isalpha()):
            print 'You did not enter yes(y) or no(n), please enter yes(y) or no(n)'
        else:
            restart = True
            break
    while not(answeredAge) and not(restart) and stillEligible:
        try:
            age = float(raw_input('Please enter your age on November 8, 2016:    '))
            if age >= 35:
                answeredAge = True
            else:
                restart = True
                break
        except ValueError:
            print 'The value you entered is not an integer'
    while not(answeredResidency) and not(restart) and stillEligible:
        try:
            resident = float(raw_input('Please enter the number of years you have lived in the US:    '))
            if resident >= 14:
                print 'You are eligible to run in the 2016 election for President of the United States'
                answeredResidency = True
            else:
                print 'You are ineligible'
                stillEligible = False
        except ValueError:
            print 'The value you entered is not an integer'
    if restart == True:
        print 'You are ineligible.'
        time.sleep(1)
        print 'Terminating program in 5 seconds...'
        time.sleep(5)
        break
