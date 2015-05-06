'''
File: wordgame.py
Authors: put your last names here
Description:
    Implements a word guessing game similar to Hangman
'''

# Import statement: DO NOT delete these! DO NOT write code above this!
import random
import time

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
    print 'Type play() and press Enter to play a game!'
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
secret_word = get_word() #Change this to get_word when ready
already_guessed = []


def print_guessed():
    
    for char in secret_word: #Check secret_word for characters shared with\
        #word_so_far
        if char in word_so_far:
            print char, #If shared, print the letter
        else:
            print "_", #If not shared, print underscores
    print "\n" #Line break

def play():
    attempts = 5 #Sets maximum number of incorrect guesses to 5
    won = False #Game over controller
    global word_so_far
    word_so_far = '' #Empty variable that raw_input will add to
    while attempts > 0 and won == False:
        print_guessed()
        time.sleep(0.5)
        guess = raw_input("Guess a letter:   ").lower()
        if guess == secret_word:
            print "You win!"
            won = True
        elif len(guess) > 1: #Only allow guesses of one letter
            print "Please only guess one letter"
            time.sleep(0.5)
        elif len(word_so_far) == len(''.join(set(secret_word))):#Win condition\
            #length of correct guess = length of word
            print "You win!"
            won = True
        elif guess in already_guessed: #Do not allow the same guess more than
            #once
            print "You have already guessed that letter. Please guess another" \
                  " letter"
        elif not(guess.isalpha()): #Do not allow numbers to be guessed
            print "Please enter a letter"
        elif guess not in secret_word: #Incorrect letter reduces attempts by 1
            already_guessed.append(guess)
            attempts -= 1
            print "Try again"
            time.sleep(1)
            print str(attempts) + " attempts remaining"
            time.sleep(0.5)
        else: #Correct letter guess replaces associated dashes with that letter
            already_guessed.append(guess)
            word_so_far += guess
    if attempts == 0: #Lose condition
        print "Game over."
        print "The word was:  " , secret_word

    
