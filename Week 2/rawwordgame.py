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

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # infile: file
    infile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = infile.read()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    print 'Type play_wordgame() and press Enter to play a game!'
    return wordlist

# load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[random.randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6


def print_guessed(secret_word, letters_guessed):
    '''
    Receives two string arguments called secret_word and letters_guessed
    Returns a string which is the string secret_word with a dash used
    to replace each character that has not yet been guessed by the player  
    '''

    word_so_far = ''
    
    ####### YOUR CODE HERE ######
    pass # This tells your code to skip this function; delete it when you
         # start working on this function

    return word_so_far


def play_wordgame():
    # play the game

    secret_word = 'inspiration'
    
    #change this to secret_word=get_word() when you are ready to start playing
    #with random words generated by the program

    guesses_made = 0

    ####### YOUR CODE HERE ######
    return None

    
