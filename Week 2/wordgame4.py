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
#secret_word = get_word() #Change this to get_word when ready
#already_guessed = []
MAX_GUESSES = 20 #Sets maximum number of incorrect guesses to 5


def print_guessed(secret_word, letters_guessed):
    """Checks the characters in the secret word to see if guessed letter
       is within the word. Replaces letters with a dash if the letter has
       not been guessed, and shows the letter if letter is guessed.
    """
    for char in secret_word: #Check secret_word for characters shared with\
        #word_so_far
        if char in word_so_far:
            print char, #If shared, print the letter
        else:
            print "_", #If not shared, print underscores
    print #Line break
    sorted(already_guessed)
    already_guessed.sort()
    print "You've already guessed:  ", already_guessed
    print
    
def play_wordgame():
    won = False #Game over controller
    global MAX_GUESSES
    global already_guessed
    already_guessed = []
    global word_so_far
    word_so_far = '' #Empty variable that raw_input will add to
    global secret_word
    secret_word = get_word() #change to secret_word = get_word() when ready
    while MAX_GUESSES > 0 and won == False:
        print_guessed(secret_word, already_guessed)
        if len(word_so_far) == len(''.join(set(secret_word))):#Win condition\
            #length of correct guess = length of word
            print "You win!"
            won = True
            break
        print "The word is", len(secret_word), "letters long"
        guess = raw_input("Guess a letter or a word:   ").lower()
        print '-------------------------------------------------------------------'
        if guess == secret_word:
            print "You win!"
            won = True
        elif len(guess) > 1 and not(guess == secret_word):
            print "Please only guess one letter at a time."
        elif guess in already_guessed: #Do not allow the same guess more than
            #once
            print "You have already guessed that letter. Please guess another" \
                  " letter"
        elif not(guess.isalpha()): #Do not allow numbers to be guessed
            print "Please enter a letter"
        elif guess not in secret_word: #Incorrect letter reduces max_guesses by 1
            already_guessed.append(guess)
            MAX_GUESSES -= 1
            print "Try again"
            print str(MAX_GUESSES) + " attempts remaining"
        else: #Correct letter guess replaces associated dashes with that letter
            already_guessed.append(guess)
            word_so_far += guess
    if MAX_GUESSES == 0: #Lose condition
        print "Game over."
        print "The word was:  " , secret_word
    if won == True:
        play_again = raw_input("Good job! Do you want to play again? Yes(y) or No(n)   ").lower()
        if play_again.isalpha() and play_again in ['yes','y']: #if entry is yes or y
            print 'Okay! Restarting in 3 seconds...'
            time.sleep(3)
            won = False
            already_guessed = []
            secret_word = get_word()            
            play_wordgame()
            
        elif not(play_again.isalpha()):
            print 'You did not enter yes(y) or no(n), please enter yes(y) or no(n)'
        else:
            print 'All right, thanks for playing!'
    guesses_made = 0
    return None
    
