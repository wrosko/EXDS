

string1 = raw_input('Please enter the DNA sequence for string 1: ').upper()
print string1
result = [string1.strip('ACTG')]
print
print
if result == ['']:      #Make a while loop here
    print
else:
    print 'invalid sequence'
    
string2 = raw_input('Please enter the DNA sequence for string 2: ').upper()
print string2
result = [string2.strip('ACTG')]
print
print
if result == ['']:      #Make a while loop here
    print
else:
    print 'invalid sequence'

