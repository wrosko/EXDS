

seqletters = 'ACTG'

string1 = raw_input('Please enter the DNA sequence for string 1: ').upper()
print seqletters
print string1

if not(any(seqletters in string1)):
        print 'String 1 is not a valid sequence'
        
#string2 = raw_input('Please enter the DNA sequence for string 2: ').upper()
#if not("A" in string1) or not("C" in string1) or not("T" in string1) or not("G" in string1):
  #  print 'Not a valid DNA sequence for string 1'
#elif not("A" in string2) or not("C" in string2) or not("T" in string2) or not("G" in string2):
  #  print 'Not a valid DNA sequence for string 2'
#else:
 #   print 'hi'
