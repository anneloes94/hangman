# Hangman game
#

# -----------------------------------


import random
import sys

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
    print(str(len(wordlist)) + " words loaded." + "\n")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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

    secretWord = list(dict.fromkeys(secretWord))
    correctlyGuessedLetters = ''
    for letter in secretWord:
        if letter in lettersGuessed: correctlyGuessedLetters += letter # lettersRead: correctly guessed letters
        else: 
          return False
    
    if len(correctlyGuessedLetters) == len(secretWord): # checks whether it's done reading all the letters
      return True    



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    shownLetters = ''
    for letter in lettersGuessed:
      if letter in secretWord:
        shownLetters += letter
    # shownLetters: all the letters that are in lettersGuessed AND in secretWord
   
    shownWord = '' 
    for letter in secretWord:
      if letter in shownLetters:
        shownWord += str(letter) + " "
      else: 
        shownWord += "_ "
    return shownWord


import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for letter in alphabet:
      if letter not in lettersGuessed:
        availableLetters += letter
    return availableLetters
    

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
    
    print("Welcome to the game Hangman!")
    print("This word contains " + str(len(secretWord)) + " letters.")
    
    numberOfMistakes = 0
    allowedNumberOfGuesses = 8
    lettersGuessed = []
    while numberOfMistakes < allowedNumberOfGuesses and (isWordGuessed(secretWord, lettersGuessed) == False):
      print ("You have " + str(allowedNumberOfGuesses - numberOfMistakes) + " guesses left.")
      print ("Available letters: "+ str(len(getAvailableLetters(lettersGuessed))))
      print ("Please guess a letter: ")
      guess = raw_input()
      guessInLowerCase = guess.lower()
      
      if guessInLowerCase in lettersGuessed:
          print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
          continue
      else:
        lettersGuessed.append(guessInLowerCase)
        
      if guessInLowerCase in secretWord:
        print ("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
      elif guessInLowerCase not in secretWord:
        numberOfMistakes += 1
        print ("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
        
    if isWordGuessed(secretWord, lettersGuessed): 
      print ("Congratulations, you won!")
    elif isWordGuessed(secretWord, lettersGuessed) == False: 
    	print ("Sorry, you ran out of guesses. The word was " + str(secretWord) + ".")

secretWord = chooseWord(wordlist)
hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
