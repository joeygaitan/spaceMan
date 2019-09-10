#Inspired by spaceman project spec from the make school.
import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    # this is a dictionary to help check for inputs to  see if you won or not
    secretDict = {} 
    # this for loop looks for characters key values  that arent in the dictionary ("a": 0)
    for letter in secret_word:
        if letter not in secretDict:
            secretDict[letter] = 0
    #This is for counting the guessed letters. It adds them into the key value
        for guessLetter in letters_guessed:
            if letter == guessLetter:
                print(letter,guessLetter)
                secretDict[letter] += 1

    # This looks for the and zeros. If it finds a zero then the game is a still on
    for secret_wordletter in secret_word:
        if secretDict[secret_wordletter] == 0:
            return False
    return True

# This shows the word you typed in or - if you didn't type anything
def get_guessed_word(secret_word, letters_guessed):
    # this is a dictionary to help check for inputs to  see if you won or not
    secretDict = {} 
    # string that will be displayed to the user
    string = ""
    # this for loop looks for characters key values  that arent in the dictionary ("a": 0)
    for letter in secret_word:
        if letter not in secretDict:
            secretDict[letter] = 0
    #This is for counting the guessed letters. It adds them into the key value
        for guessLetter in letters_guessed:
            if letter == guessLetter:
                print(letter,guessLetter)
                secretDict[letter] += 1
    #This looks for the zeros so it can fill in the missing letter with a underscore
    for secret_wordletter in secret_word:
        if secretDict[secret_wordletter] == 0:
            string += "-"
        else:
            string += secret_wordletter
    return string

# This function checks if the guess is one of the
# characters in the sectet word. It will return
# a true value if so or a false if not
def is_guess_in_word(guess, secret_word):
    # This is dictionary is for building an for the guess word. If the secret word 
    guessDictionary = {}
    for letter in secret_word:
        if guess == letter:
            return True
        else:
            return False

def userInputStart(promtps):
    userInput = input(promtps)[:1]
    return userInput

# This checks for user guessed input. 
# It filters out other non analphabetical
# chatacters and only allows one character
#  at a time.
def guessInput(promtps):
    userInput = input(promtps)
    if userInput == "Quit":
        print("Thanks for playing game")
        return "quit game"
    if len(userInput) <= 1 or "" != userInput:
        if userInput.isalpha():
            return userInput.upper()
        else:
            return guessInput("Please input only analphabetical character")
    else:
        return guessInput("please only input one character")

# This is for the user to start the game
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

    letters_guessed = []
    falseCount = 0
    runningIntro = True
    runningGame = True
    while runningIntro:
        selections= userInputStart("""\n Hi Welcome to spaceman. press m if you would like to learn more about
        the game and rules. Press P if you would like to Play. To Quit please press Q: """)
        runningIntro = selectStart(selections)
        if runningIntro == "Quit":
            runningIntro = False
            runningGame = False
            print("Thanks for trying out the Program :)")
            return ""
    while runningGame:
        # 2 function calls. One displays the word with - where the user hasn't guessed yet. The other check if you won yet or not.
        wordDisplay = get_guessed_word(secret_word, letters_guessed)
        winCheck = is_word_guessed(secret_word, letters_guessed)
        print("\nIf you would like to quit simply type (quit Game)\n")
        userGuess = guessInput(f"Please Guess an input\n Tries left: {falseCount}\n guess word {wordDisplay or ''}")
        letterCheck = is_guess_in_word(userGuess, secret_word)
        if userGuess == "Quit":
            print("\n Thanks for playing! \n")
            return spaceman(load_word())
        elif falseCount == 7:
            print(f"Dang you lost. Here's the word you tried for{secret_word}. You can always try again <3. I wish you luck in the next code you run!")
            return spaceman(load_word())
        elif letterCheck == False:
            letters_guessed.append(userGuess)
            falseCount += 1
            print(f"dang you guessed wrong. You have {7-falseCount} guesses left\n\n")
        elif letterCheck == True:
            letters_guessed.append(userGuess)
            print("Awesome you guessed right!")
        elif letterCheck == "Double":
            print("You typed  in  the same guess! I'll let it slide this time >:[")
        elif winCheck == True:
            print("Great scotts you won!!!!!")
            return spaceman(load_word())
        

        
# words = is_guess_in_word("stuff",secret_word)
# return secret_word






#These function calls that will start the game
secret_word = load_word()
print(spaceman(secret_word))