# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is", len(random.choice(wordlist)), "letters long."
    return random.choice(wordlist)
    
    
    

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = False
    check_word = []
    for letter in secretWord:
        
        if letter in lettersGuessed:
            check_word.append(letter)
           
    if len(check_word) == len(secretWord):
        result = True
           
    return result
#

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessed_word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word   
#secretWord = 'apple' 
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))
        



#import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters =''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alph:
        if letter not in lettersGuessed:
            available_letters+= letter
    return available_letters        
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    count = 8
    lettersGuessed = []
    global lettersGuessed
    
   
    
          
        
    while count >0:
            
	print ("-------------")
	print ("You have",  count,  "guesses left.")
	alph = "abcdefghijklmnopqrstuvwxyz"
        
        if len(lettersGuessed) == 0:
            print ("Available letters:", alph) 
        else:
	    print ("Available letters:", available_letters_fact)
    
	letterGuessed = raw_input("Please guess a letter:")
	if letterGuessed in lettersGuessed: 
	    
	    
	    print ("Oops! You've already guessed that letter:", guess_word_fact)  
	    continue
                           
	lettersGuessed  += letterGuessed
              
	result_fact = isWordGuessed(secretWord, lettersGuessed)
	guess_word_fact = getGuessedWord(secretWord, lettersGuessed)    
	available_letters_fact = getAvailableLetters(lettersGuessed) 
	    
	if letterGuessed in secretWord:
    
	    print ("Good guess:", guess_word_fact) 
	else:
	    print ("Oops! That letter is not in my word:", guess_word_fact)
	    count -=1
	
        if result_fact== True:
	    
	    print ("------------")
	    print ("Congratulations, you won!")
	    break
	    
    
    if not result_fact:	
        print ("-----------")
        print ("Sorry, you ran out of guesses. The word was else.") 
                  
            
             
        
    



             
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print secretWord
hangman(secretWord)



#Loading word list from file...
#55900 words loaded.
#Welcome to the game, Hangman!
#I am thinking of a word that is 4 letters long.
#-------------
#You have 8 guesses left.
#Available letters: abcdefghijklmnopqrstuvwxyz
#Please guess a letter: a
#Good guess: _ a_ _