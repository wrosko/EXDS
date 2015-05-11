'''
File: wordgame.py
Authors: put your last names here
Description:
    Implements a word guessing game similar to Hangman
'''

# Import statement: DO NOT delete these! DO NOT write code above this!
import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import words for the game

WORDLIST_FILENAME = "words.txt"

def load_words(afile):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # infile: file
    infile = open(afile, 'r')
    # line: string
    line = infile.read()
    # wordlist: list of strings
    wordlist = line.split()
    new_wordlist = []
    numa = 0
    for word in wordlist:
        if not(word.startswith('a')):
            new_wordlist.append(word)
        else:
            numa += 1
    print 'There were',numa,"words that start with a"
    print 'There are',len(wordlist),'words in wordlist'
    print 'There are',len(new_wordlist),'words in new_wordlist'
    

def load(file_name):
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # infile: file
    infile = open(file_name, 'r')
    # line: string
    line = infile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    print infile.readline()
    
    return wordlist



   

    
