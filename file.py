def is_word_guessed(secret_word, letters_guessed):
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
            return 
    return True