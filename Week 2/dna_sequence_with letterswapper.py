
import time

def strings():
    str1 = False
    str2 = False
    while True:    
        while not(str1):
            global string1
            string1 = raw_input('Please enter the DNA sequence for string 1: ').lower()
            print string1
            result = [string1.strip('actg')]
            print
            print
            if result == ['']:      #Make a while loop here
                str1 = True
                break
            else:
                print 'You did not enter a valid DNA sequence. Please enter a valid' \
                  'DNA sequence'

        while not(str2):
            global string2
            string2 = raw_input('Please enter the DNA sequence for string 2: ').lower()
            print string2
            result = [string2.strip('actg')]
            print
            print
            if result == ['']:      #Make a while loop here
                str2 = True
                break
            else:
                print 'You did not enter a valid DNA sequence. Please enter a valid' \
                  ' DNA sequence'
        break

def add_indel():
    while True:
        newindel = False
        while newindel == False:
            add = raw_input('Would you like to edit: \n a.string 1\n b.' \
                            'string 2 \n:').lower()
           # index = raw_input('At which index:  ')
            if add.isalpha() and add == 'a':
                str_1_list=list(string1)
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list))
                print "".join(map(str, cnt_str1))
                add_str1 = raw_input('Please choose a character to add:    ').lower()
                loc_str1 = int(raw_input('Before which numbered character should it be added?    '))
                str_1_list.insert(loc_str1, add_str1)
                print "".join(str_1_list)
                
                
                newindel = True
            elif add.isalpha() and add == 'b':
                str_2_list=list(string2)
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                #add_str2 = '-'
                #add_str2 = raw_input('Please choose a character to add:    ').lower()
                loc_str2 = int(raw_input('Before which numbered character should it be added?    '))
                str_2_list.insert(loc_str2, '-')
                print "".join(str_2_list)
                
                newindel = True
            else:
                print 'incorrect input'
        break
    

def dna_sequencer():
    strings()
    while True:
        sequence = False
        while sequence == False:
            entry = raw_input('What would you like to do? \n'
                      'a. press a to add an indel \n'
                      'b. press d to delete and indel \n'
                      'c. press s to find the score of the current alignment \n'
                      'd. press q to quit \n:').lower()
            if entry.isalpha() and entry in ['a']:
                print "Let's add an indel"
                time.sleep(1)
                print string1
                add_indel()

                
                sequence = True
            elif entry.isalpha() and entry in ['d']:
                print 'Deleting an indel'
                sequence = True
            elif entry.isalpha() and entry in ['s']:
                print 'Computing score'
                sequence = True
            elif entry.isalpha() and entry in ['q']:
                print 'quit'
                sequence = True
            else:
                print 'You did not input a recognized option. Please retry.'
                
        break
        
    
    
