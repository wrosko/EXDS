
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
                print 'ERROR '
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
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list))
                print "".join(map(str, cnt_str1))
                loc_str1 = raw_input('Before which numbered character should it be added?    ')
                print
                if loc_str1.isdigit() and int(loc_str1) in cnt_str1:
                    loc_str1_1 = int(loc_str1)
                    str_1_list.insert(loc_str1_1, '-')
                elif loc_str1.isdigit():
                     print 'ERROR That number is out of the index range, please input a valid number next time.'
                     print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                
                newindel = True
            elif add.isalpha() and add == 'b':
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                loc_str2 = raw_input('Before which numbered character should it be added?    ')
                if loc_str2.isdigit() and int(loc_str2) in cnt_str2:
                    loc_str2_2 = int(loc_str2)
                    str_2_list.insert(loc_str2_2, '-')
                elif loc_str2.isdigit():
                     print 'ERROR That number is out of the index range, please input a valid number next time.'
                     print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                newindel = True
            else:
                print 'incorrect input'
        break
    
def del_indel():
    while True:
        delindel = False
        while delindel == False:
            prompt = raw_input('Would you like to edit: \n a.string 1\n b.' \
                            'string 2 \n:').lower()
            if prompt.isalpha() and prompt == 'a':
                print "".join(str_1_list)
                cnt_str1 = range(len(str_1_list))
                print "".join(map(str, cnt_str1))
                delete = raw_input('Please choose which number to delete: ')
                print
                if delete.isdigit() and int(delete) in cnt_str1:
                    delete_1 = int(delete)
                    del str_1_list[delete_1]
                    print "".join(str_1_list)
                elif delete.isdigit():
                    print 'ERROR That number is out of the index range, please input a valid number next time.'
                    print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                #delindel = True
            elif prompt.isalpha() and prompt == 'b':
                print "".join(str_2_list)
                cnt_str2 = range(len(str_2_list))
                print "".join(map(str, cnt_str2))
                delete = raw_input('Please choose which number to delete: ')
                print
                if delete.isdigit() and int(delete) in cnt_str2:
                    delete_2 = int(delete)
                    del str_2_list[delete_2]
                    print "".join(str_2_list)
                elif delete.isdigit():
                    print 'ERROR That number is out of the index range, please input a valid number next time.'
                    print
                else:
                    print 'ERROR Please input a number next time.'
                    print
                delindel = True
            break
        break
        
def score(str_1_list,str_2_list):
    score_1_list = str_1_list
    score_2_list = str_2_list
    match = 0
    mismatch = 0
    if range(len(str_1_list))== range(len(str_2_list)):
        print
    elif len(score_1_list) < len(score_2_list):
        while len(score_1_list) < len(score_2_list):
            score_1_list.append('-')
        print "".join(score_2_list)
        print "".join(score_1_list)
    elif len(score_2_list) < len(score_1_list):
        while len(score_2_list) < len(score_1_list):
            score_2_list.append('-')
        print "".join(score_2_list)
        print "".join(score_1_list)
    else:
        print

    for i, (a,b) in enumerate(zip(score_1_list,score_2_list)):
        if a == b:
            match +=1
        else:
            score_1_list[i] = a.upper()
            score_2_list[i] = b.upper()
    mismatch = min(len(score_1_list),len(score_2_list))-match
    print match
    print mismatch

        
    '''for i in range(len(score_1_list)):
        if score_1_list is score_2_list:
            match = int(len(score_1_list))
            
        elif score_1_list[i] == '-':
            mismatch += 1
            return mismatch
            if score_1_list[i].isalpha():
                score_1_list[i].upper()
                return score_1_list
            else:
                print
        elif score_2_list[i] == '-':
            mismatch += 1
            return mismatch
            if  score_2_list[i].isalpha():
                 score_2_list[i].upper()
                 return score_2_list
            else:
                print
        else:
            mismatch += 1
            score_1_list[i].upper()
            score_2_list[i].upper()
            return mismatch,score_1_list,score_2_list
            #if str_1_list[i] or str_2_list[i] == '-' '''
    
    #for a,b in zip(str_1_list, str_2_list):
            #if a or b == '-':
             #   mismatch += 1
            #elif a == b:
             #   match += 1
            #elif a != b:
             #   mismatch += 1
              #  a.upper()
               # b.upper()
            #else:
            #    print
   # print match
    #print mismatch
    #print str_1_list
    #print str_2_list
    print "".join(score_1_list)
    print "".join(score_2_list)
                

            
    

def dna():
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
                      'b. press d to delete an indel \n'
                      'c. press s to find the score of the current alignment \n'
                      'd. press q to quit \n:').lower()
            print
            if entry.isalpha() and entry in ['a']:
                print "Let's add an indel"
                time.sleep(1)
                add_indel()
                #print string1
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
                score(str_1_list,str_2_list)
                #sequence = True
            elif entry.isalpha() and entry in ['q']:
                print 'quit'
                sequence = True
            else:
                print 'You did not input a recognized option. Please retry.'
                
        break
        
    
    
