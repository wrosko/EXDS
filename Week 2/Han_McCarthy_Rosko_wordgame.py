'''
File: Han_McCarthy_Rosko_wordgame.py
Authors: Han, McCarthy, Rosko
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
    print #Line break
    for char in secret_word: #for each character in secret_word
        if char in letters_guessed: #checks if the char. is in letters_guessed
            print char, #if true prints the character
        else:
            print '_', #if not true prints a dash for letters not guessed
    print 
    return word_so_far


def play_wordgame():
    # play the game

    secret_word = get_word()
    guesses_made = 0

    '''
    Runs the program. Requires no arguments. It will prompt for user input.
    Will take into account repeated guesses, non-alphabetic characters, and
    guesses exceeding one character. Each time the user inputs a new incorrect
    entry, it will add to the variable guesses_made. Then it will find the
    difference between MAX_GUESSES and incorrect guesses_made.
    '''
    won = False
    already_guessed = [] #empty list that is added to
    letter_counter = 0 #counter variable
    while MAX_GUESSES - guesses_made > 0 and won == False: #loop conditions
        print_guessed(secret_word, already_guessed) #calls on print_guessed
                                                    #with constraints
        while letter_counter <= len(secret_word): #checks to see if
                                                  #counter is <=length of
                                                  #secret_word
            try:
                if secret_word[letter_counter] in already_guessed:
                    letter_counter += 1 #adds 1 to letter_counter if
                                        #indexed character of secret_word
                                        #is in already_guessed
                else:
                    break
            except IndexError:
                print "You win!" #If it returns an index error, all char 
                won = True       #will be in already_guessed
                break
        if won == True: 
            break #breaks out of loop
        print 'The word is', len(secret_word), 'letters long.'
        print str(MAX_GUESSES - guesses_made) + ' attempts remaining.'
        #attempts remaining provided to player
        guess = raw_input('Guess a letter:  ').lower()
        print '_______________________________________________________________'
        if len(guess) > 1:
            print 'Please only guess one letter at a time.'
        elif guess in already_guessed:
            print 'You have already guessed that letter. Please guess another.'
        elif not(guess.isalpha()):
            print 'Please only enter an alphabetic character.'
        elif guess not in secret_word:
            already_guessed.append(guess)#add guess to already_guessed
            guesses_made += 1            #list. Add 1 to guesses_made
            print 'Sorry, that\'s not right.'
        else:
            already_guessed.append(guess)#valid guess, correct guess, not in
                                    #already_guessed. Adds to already_guessed
    if MAX_GUESSES - guesses_made == 0:#Algebra. Takes constant and subtracts
                                       #incorrect guesses_made
        print 'Too many incorrect guesses!'
        print 'The word I was thinking of was',secret_word
        print 'Game over. You lost.'
    return None 
