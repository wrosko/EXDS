'''
File: Dunleavy_Rosko_textanalysis.py
Authors: Dunleavy, Rosko
Description: A text analysis program that counts the number of unique words
    in a text file. It then prints the unique words, and the number of their
    occurences in the file. The program makes use of the regular expressions
    built in module.
'''

import re #import the regular expressions built in module

print "Please enter textanalysis('Your_File_Name_Here') to run the analysis"
print #Prompting the user to call on the main function with the file name
      #as an argument.

def textanalysis(filename):
    """
    Main function that opens a text file. It calls on two other functions.
    Stores the contents of the file as a global variable. It prints the
    number of unique words and their occurences.
    """
    
    infile = open(filename,'r')
    global line1    #establishes the variable line1 as global
    line1 = infile.read()
    infile.close()

    text_modifier()
    print
    uniquewordlist()
    

def text_modifier():
    """
    Splits the global variable defined as the contents of the file into lists
    by using the regular expression module and the split() command. Defines
    a global variable LIST3 that contains the unique words in the text file.
    """
    
    #regular expression module is used to go through line1 and replace
    #anything that is not alphabetic or a space with a space. The result is
    #stored as the variable line.
    line = re.sub("[^a-zA-Z+\s]"," ",line1)
    LIST = [] #define a new list

    #Split line into a list at every new line
    bigwordlist = line.split('\n')
    #For each entry in bigwordlist, split the entry into a list at each space.
    #Then add each entry into a new list. The result is sublists within a list.
    for c in bigwordlist:
        bigwordlist1= list(c.split(' '))
        LIST.append(bigwordlist1)
    
    #LIST2 is created without any sublists.
    LIST2= [item for sublist in LIST for item in sublist]
    
    global LIST3 #define LIST3 as global
    LIST3 = []#Create new list
    #Adds entries to LIST3 that are just words and not spaces. Changes any
    #uppercase to lowercase.
    for c in LIST2:
        if c != '':
            LIST3.append(c.lower())
    
    print "The number of unique words in the text is", len(LIST3)
    

def uniquewordlist():
    """
    Creates a set of all of the unique words in the file, and then prints
    them and the number of their occurences.
    """
    #Create a set of all unique words.
    unique_words = set(LIST3)
    #define a new list that has each unique word and its occurences.
    occurences = [[x,LIST3.count(x)] for x in unique_words]
    
    print 'Below is a list of each unique word and its frequency.'
    print
    for c in occurences: #Prints the occurences in a vertical list
        print c


        
        

    
            

    
