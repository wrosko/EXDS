def add_indel(DNAstr):
    # the adding indel function. 
    #string_choice = raw_input('Work on which string (1 or 2): ')
    index = int(raw_input('Before what index: ')) 

##    if string_choice == '1':

    #This loop ensures that the index is not out of range
    while index > len(DNAstr) or index < 0:
        print ('Error. Index out of range.')
        index = int(raw_input('Before what index: '))
            
        #adds an indel before the index by concatenating string 1
        #upto postion index-1, a dash and the rest of the string
    DNAstr = DNAstr[:index] + '-' + DNAstr[index:]
    return DNAstr
    
        
##    if string_choice == '2':
##        while index > len(DNA_str_2) or index < 0:
##            print ('Error. Index out of range.')
##            # gives an error message if the index provided
##            #is out of range
##            index = int(raw_input('Before what index: '))
##            
##        #adds an indel before the index by concatenating string 2
##        #upto postion index-1, a dash and the rest of the string
##        DNA_str_2 = DNA_str_2[:index] + '-' + DNA_str_2[index:]
        

def delete_indel(DNAstr):

    #string_choice = raw_input('Work on which string (1 or 2): ')
    index = int(raw_input('At what index: '))


        #This loop ensures that the index is not out of range
    while index > len(DNAstr) or index < 0:
        print ('Error. Index out of range.')
        index = int(raw_input('At what index: '))
            
        #This loop ensures that the character at index is
        #an indel
    while DNAstr[index] != '-':
        print ('Error. Cannot delete a character that is not an indel.')
        index = int(raw_input('At what index: '))

        #deletes an indel at the index by concatenating string 1
        #upto postion index-1 and the rest of the string
        #starting at index+1.   
    DNAstr = DNAstr[:index] + DNAstr[index + 1:]
        
    return DNAstr

def score():
    
    global DNA_str_1
    global DNA_str_2
      
    matches = ""
    mismatches = ""
    
    #fill the sequence with fewer letters with dashes
    if len(DNA_str_1) != len(DNA_str_2):
        
        if len(DNA_str_1) > len(DNA_str_2):
            diff = len(DNA_str_1) - len(DNA_str_2)
            msequence_1 = DNA_str_1
            msequence_2 = DNA_str_2 + diff * "-"                       
        
        else:
            diff = len(DNA_str_2) - len(DNA_str_1)
            msequence_1 = DNA_str_1 + diff * "-"
            msequence_2 = DNA_str_2
            
    else:
        msequence_1 = DNA_str_1
        msequence_2 = DNA_str_2

    #change the matched letters to lower case
    #change the mismatched ones to upper case
    s = range(len(msequence_1))
    
    for c in s:
        if msequence_1[c] == msequence_2[c]:
            msequence_1 = msequence_1[:c] + msequence_1[c].lower() + \
                          msequence_1[c+1:]
            msequence_2 = msequence_2[:c] + msequence_2[c].lower() + \
                          msequence_2[c+1:]
        else:
            msequence_1 = msequence_1[:c] + msequence_1[c].upper() + \
                          msequence_1[c+1:]
            msequence_2 = msequence_2[:c] + msequence_2[c].upper() + \
                          msequence_2[c+1:]

    mismatches = sum(msequence_1[i] != msequence_2[i]\
                     for i in range((len(msequence_1))))
    matches = len(msequence_1) - mismatches


    print "Matches:", matches, "Mismatches:",mismatches,\
          "\n","sequence_1:",msequence_1,\
          "\n","sequence_2:",msequence_2

    return None


# Startup dialogue asking the user for the two DNA strings to be compared.
print 'input ',
DNA_str_1 = raw_input('DNA String 1:  ')
print ''
print 'input '  ,
DNA_str_2 = raw_input('DNA String 2:  ')
print''

# The execution step. The action
# is a variable either a, d, s, or q, that executes one of the above functions
# if it's a, d, or s or ends the program if it's q.
while True :
    print 'what do you want to do?:  '
    print ''
    action = raw_input( 'a (add indel) , d (delete indel) , s (score) \
, q(quit): ')
    print ''
    if action == 'a':
        string_choice = raw_input('Work on which string (1 or 2): ')
        if string_choice == '1':
            DNA_str_1 = add_indel(DNA_str_1)
        elif string_choice == '2':
            DNA_str_2 = add_indel(DNA_str_2)
        else:
            print
    else:
        if action == 'd':
            string_choice = raw_input('Work on which string (1 or 2): ')
            if string_choice == '1':
                DNA_str_1 = delete_indel(DNA_str_1)
            elif string_choice == '2':
                DNA_str_2 = delete_indel(DNA_str_2)
            else:
                print
        else:
            if action == 's':
                score()
            else:
                if action == 'q':
                    print '                   program ends'
                    break
                else:
                    print 'please input a valid action.' 
    


