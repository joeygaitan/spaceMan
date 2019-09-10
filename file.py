# Testing file

def get_guessed_word(secret_word, letters_guessed):
# This function checks if the game is over
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


print(get_guessed_word("hello", ["h","l"]))