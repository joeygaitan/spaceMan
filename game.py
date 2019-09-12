#Inspired by spaceman project spec from make school. <3
import random

def load_word():
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def secret_word_dictionary_matrix_builder(secret_word, letters_guessed):
    """
    This function builds a matrix dictionary with two for loops filtering the secret_word string
    into keys for the dictionary. Then it adds a number value for letters found in the list. This is
    useful potentially for catching multiple duplicates or finding missing element. 
    """
    # this is a dictionary to help check for inputs to  see if you won or not
    secretDictionary = {}
    # this for loop looks for characters key values  that arent in the dictionary ("a": 0)
    for letter in secret_word:
        if letter not in secretDictionary:
            secretDictionary[letter] = 0
    #This is for counting the guessed letters. It adds them into the key value
        for guessLetter in letters_guessed:
            if letter == guessLetter:
                secretDictionary[letter] += 1
    return secretDictionary

def is_word_guessed(secret_word, letters_guessed):
    """
    It is given an filtered dictionary with each guess checked already.
    Then it looks for and zeros. If it finds a zero then the game is a still on.
    If it finds no zeros then it returns true and you win
    """
    secretDict = secret_word_dictionary_matrix_builder(secret_word, letters_guessed)
    for secret_wordletter in secret_word:
        if secretDict[secret_wordletter] == 0:
            secretDict.clear()
            return False
    secretDict.clear()
    return True

# This shows the word you typed in or - if you didn't type anything
def get_guessed_word(secret_word, letters_guessed):
    """
    It is given an filtered dictionary with each guess checked already.
    Then it looks for any zeros inside of secretDict. If it finds any missing letter values a (zero) with a underscore
    it adds it to string otherwise it adds in the value.
    """
    secretDict = secret_word_dictionary_matrix_builder(secret_word, letters_guessed)
    string = ""
    #This looks for the zeros inside of secretDict so it can fill in the missing letter with a underscore
    for secret_wordletter in secret_word:
        if secretDict[secret_wordletter] == 0:
            string += "-"
        else:
            string += secret_wordletter
    secretDict.clear()
    return string

def duplicate_check(guess, checkedLettersString):
    """
    This is given a cleared input guess character. After it checks if its already in there.
    If it's in there then it gives return Double. Where a conditional in there
    displays you already clicked that and reruns the while loop 
    """
    for letter in checkedLettersString:
        if guess == letter:
            return "Double"
    return True

def is_guess_in_word(userGuess, secret_word):
    """
    This function checks if the guess is one of the
    characters in the sectet word. It will return
    a true value if so or a false if not
    """
    for letter in secret_word:
        if userGuess == letter:
            return True
    return False
    
def userInputStart(promtps):
    userInput = input(promtps)
    return userInput

def guessInput(promtps):
    """
    This checks for user guessed input. 
    It filters out other non analphabetical
    chatacters and only allows one character
    at a time.
    """
    userInput = input(promtps).lower()
    if userInput == "play":
        return "play"
    if userInput == "yes":
        return "yes"
    elif userInput == "no":
        return "no"
    elif userInput == "quit":
        print("Thanks for playing the game")
        return "quit"
    elif userInput == secret_word:
        return True
    elif len(userInput) <= 1 or "" != userInput:
        if userInput.isalpha():
            return userInput
        else:
            return guessInput("Please input only aphabetical character\n Type your guess here: ")
    else:
        return guessInput("please only input one character\n Type your guess here: ")

def selectStart(function_code):
    """
    This is for the user to start the game.
    It takes a few inputs.
    It returns True, False, or Quit String
    """
    if function_code == "Man" or function_code == "man":
        print("\n The game is quite simple. You can guess a letter wrong 7 times until you fail. If you get it right it doesn't count as a guess. \n")
        return True
    elif function_code ==  "play" or function_code == "Play" or function_code == "p" or function_code == "P":
        return False
    elif function_code ==  "Quit" or function_code == 'quit':
        return "Quit"
    else:
        print("\n Please Type one of the three inputs \n")
        return True

def spaceman(secret_word):
    """
    Declared 2 integers, two lists, and two booleans. The letters_guessed will soon be invoking the letter_function.
    The wrong_guessed will append whenever the user gets a false input.
    the count is decremented everytime you get a wrong input with the false conditional.
    """
    letters_guessed = []
    wrong_guessed = []
    falseCount = 7
    runningIntro = True
    runningGame = True
    while runningIntro:
        selections= userInputStart("\n Hi Welcome to spaceman. press man if you would like to learn\n more about the game and rules. Type Play if you would like to Play. To Quit please type quit: ")
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
        print("\nIf you would like to quit simply type (quit)\n")
        userGuess = guessInput(f"Please Guess an input\nTries left: {falseCount}\nFree Tip: {wordDisplay}\nIncorrect Guesses: {wrong_guessed}\n\nPlease Guess Here: ")
        duplicateCheckBoolean = duplicate_check(userGuess, wordDisplay)
        letterCheck = is_guess_in_word(userGuess, secret_word)
        if userGuess == "quit":
            print("\n Thanks for playing! \n")
            return spaceman(load_word())
        else:
            if userGuess == True:
                    print("Great scotts you won!!!!!")
                    falseCount = 7
                    secret_word = load_word()
                    letters_guessed.clear()
                    wrong_guessed.clear()
                    winInput = guessInput("If you would like to play again type Play. If you wouldn't type in no: ")
                    if winInput == "yes":
                        print("Lets go Again!")
                    elif winInput == "no":
                        print("It was fun while it lasted")
                        return ""

            elif duplicateCheckBoolean == "Double":
                print("You typed  in  the same guess! I'll let it slide this time >:{")

            elif letterCheck == True:
                letters_guessed.append(userGuess)
                print("Awesome you guessed right!")
                winCheck = is_word_guessed(secret_word, letters_guessed)
                if winCheck == True:
                    print("Great scotts you won!!!!!")
                    falseCount = 7
                    secret_word = load_word()
                    letters_guessed.clear()
                    wrong_guessed.clear()
                    winInput = guessInput("If you would like to play again type yes. If you wouldn't type in no: ")
                    if winInput == "yes":
                        print("Lets go Again!")
                    elif winInput == "no":
                        print("It was fun while it lasted")
                        return ""

            elif letterCheck == False and winCheck==False:
                if len(userGuess) != 1 or "play" == userGuess or userGuess == "yes" or "no" == userGuess:
                    print("\nNoty noty. You can't put that here >:(")
                else:
                    letters_guessed.append(userGuess)
                    wrong_guessed.append(userGuess)
                    falseCount -= 1
                    print(f"dang you guessed wrong. You have {falseCount} guesses left\n\n")

                    if falseCount == 0:
                        print(f"Dang you lost. Here's the word you were trying to guess: !!!{secret_word}!!!!. You can always try again <3. I wish you luck in the next code you run!")
                        return spaceman(load_word())

#These function calls that will start the game
secret_word = load_word() 
spaceman(secret_word)