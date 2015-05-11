"""
File: Han_McCarthy_Rosko_dnamatching.py
Authors: Han, McCarthy, Rosko
Description: DNA sequencer. Allows a user to input two sequences of DNA
    and then gives them the ability to add and delete indels, as well as find
    the score of the two sequences.
"""

import time #imports time package 

def strings():
    
    """
    The strings function asks for user imput for a dna sequence.
    It only accepts the input if the characters entered are A, C, T,
    or G.
    Receives: raw input
    Returns: string variables
    """
    
    str1 = False
    str2 = False
    while True:    
        while not(str1):
            
#Establish string1 as global so it can be called on by any of the other
#functions. This value and string2 will not be changed by any other function.
#They will be constants. Other variables will be created from their data.
            
            global string1              
            string1 = raw_input('Please enter the DNA sequence for '\
                                'string 1: ').lower()
            
#result will be variable used in a boolean. Takes out all actg in entry
#if there is any other character statement will be false and user is
#prompted to re-enter the sequence
            
            result = [string1.strip('actg')] 
            print
            if len(string1) > 0:  
                if result == ['']:      
                    str1 = True
                    break
                else:       #if enter is hit, it will prompt for
                    print 'ERROR ' #the entry again
                    print 'You did not enter a string. Please enter a string.'
            else:
                print 'ERROR '
                print 'You did not enter a valid DNA sequence. Please enter '\
                      'a valid DNA sequence'

#same chunk of code as for string1
        while not(str2):
            global string2 
            string2 = raw_input('Please enter the DNA sequence for ' \
                                'string 2: ').lower()
            result = [string2.strip('actg')]
            print
            if len(string2) > 0:
                if result == ['']:      
                    str2 = True
                    break
                else:
                    print 'ERROR '
                    print 'You did not enter a string. Please enter a string.'
            else:
                print 'ERROR '
                print 'You did not enter a valid DNA sequence. Please enter '\
                      'a valid DNA sequence'
        break

def add_indel():
    
    """
    add_indel prompts for which string the user would like to edit
    it then displays the sequence with the index below it. The user enters the
    position where the indel is added.
    Receives: converted sequence (list) *converted means it is not the original
    string1 or string2. They have been converted to lists.
    Returns: modified sequence with indel (list)
    """
    
    while True:
        newindel = False
        while newindel == False:
#ask for user input to choose string1 or string2
            add = raw_input('Would you like to edit: \n a.string 1\n b.' \
                            'string 2 \n:').lower()
            if add.isalpha() and add == 'a':
                print "".join(str_1_list) #the converted list will appear
                                     #as a string
                cnt_str1 = range(len(str_1_list)) #range gives index list
                                                  #map() and str display the
                print "".join(map(str, cnt_str1)) #index nums of the sequence
                print
                loc_str1 = raw_input('Before which numbered character should'\
                                     ' it be added?    ')
                print
                
#if loc_str1 is a number and it is in the index, a - is added at the index
                
                if loc_str1.isdigit() and int(loc_str1) in cnt_str1:
                    loc_str1_1 = int(loc_str1)
                    str_1_list.insert(loc_str1_1, '-')
                elif loc_str1.isdigit():
                     print 'ERROR That number is out of the index range, '\
                           'please input a valid number next time.'
                     print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                
                newindel = True
                
#same code as above just with variables changed for string2
                
            elif add.isalpha() and add == 'b':
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                print
                loc_str2 = raw_input('Before which numbered character should'\
                                     ' it be added?    ')
                if loc_str2.isdigit() and int(loc_str2) in cnt_str2:
                    loc_str2_2 = int(loc_str2)
                    str_2_list.insert(loc_str2_2, '-')
                elif loc_str2.isdigit():
                     print 'ERROR That number is out of the index range, '\
                           ' please input a valid number next time.'
                     print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                newindel = True
            else:
                print 'incorrect input'
        break
    
def del_indel():
    
    """
    The same function as add_indel except that it will delete value
    at a given index. The user chooses which string and the index.
    Receives: converted sequence (list)
    Returns: modified sequence with indel (list)
    """
    
    #The following code and logic is very similar to add_indel
    
    while True:
        delindel = False
        while delindel == False:
            prompt = raw_input('Would you like to edit: \n a.string 1\n b.' \
                            'string 2 \n:').lower()
            if prompt.isalpha() and prompt == 'a':
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list)) #see add_indel for logic 
                print "".join(map(str, cnt_str1))#for this section
                print
                delete = raw_input('Please choose which number to delete: ')
                print
                if delete.isdigit() and int(delete) in cnt_str1:
                    if str_1_list[int(delete)] is '-':#checks to see if object
                        delete_1 = int(delete) #at the index is an indel
                        del str_1_list[delete_1] #deletes the value at the given
                    else:
                        print 'ERROR. You can only delete an indel.'
                elif delete.isdigit():
                    print 'ERROR That number is out of the index range, please'\
                          ' input a valid number next time.'
                    print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                    
#same code as above, but for string2
                    
            elif prompt.isalpha() and prompt == 'b':
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                print
                delete = raw_input('Please choose which number to delete: ')
                print
                if delete.isdigit() and int(delete) in cnt_str2:
                    if str_2_list[int(delete)] is '-':
                        delete_2 = int(delete)
                        del str_2_list[delete_2]
                    else:
                        print 'ERROR. You can only delete an indel.'
                elif delete.isdigit():
                    print 'ERROR That number is out of the index range, '\
                          'please input a valid number next time.'
                    print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                delindel = True
            break
        break
        
def score(str_1_list,str_2_list):
    
    """
    Takes a score of the two sequences. It will display the number of
    matches and mismatches. It also adds dashes to a sequence if it is shorter
    than the other until they are of equal length. It counts an indel as
    a mismatch. Mismatched characters will be capitalized if they are
    alphabetical.
    Receives: converted sequence (list)
    Returns: sequence with added indels and capitalization changes (list)
    """
    
    score_1_list = str_1_list[:] #here we make a copy of the string lists.
    score_2_list = str_2_list[:]
    
    match = 0   #setting our match variable to  zero
#The following lines check the length of the sequences and append indels to the
#end of the shorter sequence.
    
    if range(len(score_1_list))== range(len(score_2_list)):
        pass 
    elif len(score_1_list) < len(score_2_list):
        while len(score_1_list) < len(score_2_list):
            score_1_list.append('-')
    elif len(score_2_list) < len(score_1_list):
        while len(score_2_list) < len(score_1_list):
            score_2_list.append('-')
    else:
        pass
    
#from using stackoverflow we found that zip joins two lists by grouping the
#specific indices. Enumerate then assigns the indices to the pairs of the lists
    
    for i, (a,b) in enumerate(zip(score_1_list,score_2_list)):
        if a == b: #match counter increases when the two are equal
            match +=1
        else:
            score_1_list[i] = a.upper()
            score_2_list[i] = b.upper()
            
#min() looks at the len() of the two lists and takes the smallest value.
#mismatch is calculated from the difference of min() and match
            
    mismatch = min(len(score_1_list),len(score_2_list))-match
    
#matches and mismatches are displayed
    
    print 'There are',match,'matches, and',mismatch,'mismatches.'
    print 'String 1: ',"".join(score_1_list)
    print 'String 2: ',"".join(score_2_list)
    print
            
def dna_sequencer():
    """
    Main function. This calls on the strings() function. It then prompts the
    user to add or delete and indel, take the score of the sequences, or quit
    the program. It will call on the functions: strings(), add_indel(),
    del_indel(), and score().
    Establishes global variables
    """
#Initially call on strings() and then define a variable as the list of the
#string variables.
    strings()
    global str_1_list
    str_1_list=list(string1)
    global str_2_list
    str_2_list=list(string2)
    while True: #set up a loop so that it is not terminated until 'quit'
        sequence = False
        while sequence == False:
            entry = raw_input('What would you like to do? \n'
                      'a. press "a" to add an indel \n'
                      'b. press "d" to delete an indel \n'
                      'c. press "s" to compute the score of the present' \
                      ' alignment \n'
                      'd. press "q" to quit \n:').lower()
            print
            
#call on each function for the respective option.
            
            if entry.isalpha() and entry in ['a']:
                print "Let's add an indel"
                add_indel()
            elif entry.isalpha() and entry in ['d']:
                print 'Deleting an indel'
                del_indel()
            elif entry.isalpha() and entry in ['s']:
                print 'Computing score . . .'
                time.sleep(.5)
                score(str_1_list,str_2_list)
            elif entry.isalpha() and entry in ['q']:
                print 'QUIT'
                sequence = True
            else:
                print 'You did not input a recognized option. Please retry.'    
        break
        
    
    
