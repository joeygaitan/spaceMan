import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    secretDict = {}

    for letter in secret_word:
        if letter not in secretDict:
            secretDict[letter] = 0
        for guessLetter in letters_guessed:
            if letter == guessLetter:
                print(letter,guessLetter)
                secretDict[letter] += 1

    for secret_wordletter in secret_word:
        if secretDict[secret_wordletter] == 0:
            return False
    return True
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

def get_guessed_word(secret_word, letters_guessed):

    '''
    A function that is used to get a string showing the letters guessed so far in
    the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, 
        the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, 
        shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    pass

# This function checks if the guess is one of the characters in the sectet word. It will return
#  a true value if so or a false if not
def is_guess_in_word(guess, secret_word):
    for letter in secret_word:
        if guess == letter:
            return True
        else:
            return False
    # TODO: check if the letter guess is in the secret word

# This function is for displaying the wrongly guessed words
def wrongGuesses():
    pass
# This function is for displaying the letters that were guessed right
def rightGuesses():
    pass

def userInputStart(promtps):
    userInput = input(promtps)
    return userInput

# This checks for user guessed input. It filters out other non analphabetical chatacters and only allows one character at a time. 
def userInput(promtps):
    userInput = input(promtps)
    if len(userInput) <= 1 or "" != userInput:
        if userInput.isalpha():
            return userInput.upper()
        else:
            return userInput("Please input only analphabetical character")
    else:
        return userInput("please only input one character")

def selectStart(function_code):
    if function_code == "M" or function_code == "m":
        print("\n The game is quite simple. You can guess a letter wrong 7 times until you fail. If you get it right it doesn't count as a guess. \n")
        return True
    elif function_code ==  "P" or function_code == "p":
        return False
    elif function_code ==  "Q" or function_code == 'q':
        return "Quit"
    else:
        print("\n Please Type one of the three inputs \n")
        return True


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    runningIntro = True
    runningGame = True
    while runningIntro:
        selections= userInputStart("Hi Welcome to spaceman. press m if you would like to learn more about the game and rules. Press P if you would like to Play. To Quit please press Q: ")
        runningIntro = selectStart(selections)
        if runningIntro == "Quit":
            runningIntro = False
            runningGame = False
            print("Thanks for trying out the Program :)")
            return ""
    while runningGame:
          Selections = userInput()
          
        # words = is_guess_in_word("stuff",secret_word)
    # return secret_word

    #TODO: show the player information about the game according to the project spece

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
print(spaceman(secret_word))