'''
File: textanalysis_solution.py
Authors: compiled from class
Description:
    Prompts user for the name of a text file, and analyzes that file
    for the number of unique words in the text. Prints the number of
    unique words in total and also the number of times each unqiue
    word appears.
'''

import re #import the regular expressions built in module

#tells the user to call the main function
print 'To run text analysis please type: textanalysis()'

def textanalysis():
    """
    Main function that prompts the user for a text file.
    Stores the contents of the file as a list of words after
    modifying it as per the definition of word.
    Calls another function to obtain a list of unique words.
    Prints the number of unique words in the text and
    a list of unique words with their frequency.
    """

    #Prompts for text file name
    text = raw_input('Please enter the exact name of the text file '
                     'you wish to analyze:\n')
    
    infile = open(text, 'r') #Opens file

    #Reads file and stores it as a string 
    text_str = infile.read()

    #regular expression module is used to go through text_str and
    #replace anything that is not an alphabet or a space with
    #a space. The result is stored as the variable modified_text_str.
    #modified_text_str = re.sub("[^a-zA-Z+\s]"," ",text_str)

##    Here is another way to do what we just did without the use of
##    re. The result is still stored in text_str here.
    for c in text_str:
        if c.isalpha():
            pass
        else:
            text_str = text_str.replace(c,' ')

    #splits the modified string of text by whitespace,
    #and places all words into a list called wordlist
    wordlist = list(text_str.split())

    #Call the function find_unique to obtain a list of unique
    #words in the text
    unique_wordlist = find_unique(wordlist)

    #print the number of unique words in the list
    print "There are", len(unique_wordlist)," unique words in the text."

    #print the frequency of each unique word in the text by counting
    #the number of times it appears in wordlist
    for word in unique_wordlist:
        print word + ",", wordlist.count(word)
    
    return None

def find_unique(allwords):
    '''
    Receives a list of words.
    Returns a list of unique words from this list in lower case.
    '''
    #set the unique_words variable to an empty list.
    unique_words=[]
    
    #loop for each word the list allwords
    for word in allwords:

        #makes each word in lowercase 
        word=word.lower()

        #adds word to list of unique words if not already in it.
        if word not in unique_words:
            unique_words.append(word)

    return unique_words
           
    

    

    
    
    
