
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
            if result == ['']:      
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
            if result == ['']:      
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
            if add.isalpha() and add == 'a':
                #global str_1_list
                #str_1_list=list(string1)
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list))
                print "".join(map(str, cnt_str1))
                loc_str1 = int(raw_input('Before which numbered character should it be added?    '))
                str_1_list.insert(loc_str1, '-')
                print "".join(str_1_list)
                
                newindel = True
            elif add.isalpha() and add == 'b':
                #global str_2_list
                #str_2_list=list(string2)
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                loc_str2 = int(raw_input('Before which numbered character should it be added?    '))
                str_2_list.insert(loc_str2, '-')
                print "".join(str_2_list)
                
                newindel = True
            else:
                print 'incorrect input'
        break
    
def del_indel():
    while True:
        newindel = False
        while newindel == False:
            prompt = raw_input('Would you like to edit: \n a.string 1\n b.' \
                            'string 2 \n:').lower()
            if prompt.isalpha() and prompt == 'a':
               # global str_1_list
                #str_1_list=list(string1)
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list))
                print "".join(map(str, cnt_str1))
                delete = int(raw_input('Please choose which number to delete: '))
                del str_1_list[delete]
                print "".join(str_1_list)
               
                break
                
                newindel = True
            elif prompt.isalpha() and prompt == 'b':
                #global str_2_list
                #str_2_list=list(string2)
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                delete = int(raw_input('Please choose which number to delete: '))
                del str_2_list[delete]
                print "".join(str_2_list)
                break
                newindel = True
            else:
                print 'incorrect input'
        break
#def score():
    

def dna_sequencer():
    strings()
    global str_1_list
    str_1_list=list(string1)
    global str_2_list
    str_2_list=list(string2)
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
                add_indel()
                print string1
                #if promt = change string 1
                   # new_str_1 = add_indel(string1, string 2)
                #if prompt = change string 2
                   # new_str_2 = 

                
                #sequence = True
            elif entry.isalpha() and entry in ['d']:
                print 'Deleting an indel'
                del_indel()
                #sequence = True
            elif entry.isalpha() and entry in ['s']:
                print 'Computing score'
                sequence = True
            elif entry.isalpha() and entry in ['q']:
                print 'quit'
                sequence = True
            else:
                print 'You did not input a recognized option. Please retry.'
                
        break
        
    
    
