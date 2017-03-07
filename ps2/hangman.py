# Problem Set 2, hangman.py
# Name: George Mu
# Collaborators: None
# Time spent: 6:00

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"




def load_words():
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



def get_input(letters_guessed):
    '''
    guess: asks for user's raw input
    returns: user's input converted into a string if it's valid input, or it returns a warning
    '''
    guess = str.lower(str(input("Please guess a letter:")))
    if guess == '*':
        return 'help'
    elif guess == '-':
        return 'freehint'
    elif not str.isalpha(guess) or not bool(guess) or len(guess) > 1 or len(guess) < 1: # Check for all invalid inputs
        return 'invalid'
    elif guess in letters_guessed:
        return 'priorguess'
    else:
        return guess

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return all(letter in letters_guessed for letter in secret_word)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters and octothorps (#) that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    display_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            display_word = display_word + letter
        else:
            display_word = display_word + "#"
    return display_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
      letters have not yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    import string
    available_letters = ''
    starting_string = string.ascii_lowercase

    for letter in starting_string:
        if letter in letters_guessed:
            available_letters = available_letters + ''
        else:
            available_letters = available_letters + letter
    return available_letters

def available_help(secret_word, available_letters):
    '''
    secret_word: the string that is the secret word
    available_letters: the list of letters that are still available
    returns: string of unique letters in the secret_word that haven't been guessed yet
    '''
    choose_from = secret_word.join(set(available_letters))
    return choose_from

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 8 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 8
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    letters_guessed = []
    guess = ''
    warnings_left = 3

    count_unique = len(''.join(set(secret_word))) # get the number of unique characters in the secret_word

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word), 'letters long.')
    print('You have', warnings_left, "warnings left.")


    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        print('------------')
        # Print how many guesses the user has left
        if guesses_remaining > 1:
            print('You have', guesses_remaining, 'guesses left.')
        else:
            print('You have', guesses_remaining, 'guess left.')
        print('Available letters:', get_available_letters(letters_guessed))

        # Get the user guess
        guess = get_input(letters_guessed)

        # When the guess is not a valid character
        if guess == 'invalid' and warnings_left > 0:
            warnings_left -= 1
            if warnings_left == 1:
                print('Oops! That is not a valid letter. You have', warnings_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That is not a valid letter. You have', warnings_left, 'warnings left:', get_guessed_word(secret_word, letters_guessed))

        elif guess == 'invalid' and warnings_left <= 0:
            print('Oops! That is not a valid letter. You have no warnings left, so you lost a guess:', get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

        # When the guess was already guessed before
        elif guess == 'priorguess' and warnings_left > 0:
            warnings_left -= 1
            if warnings_left == 1:
                print('Oops! You already guessed that letter. You have', warnings_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! You already guessed that letter. You have', warnings_left, 'warnings left:', get_guessed_word(secret_word, letters_guessed))

        elif guess == 'priorguess' and warnings_left <= 0:
            print('Oops! You already guessed that letter. You have no warnings left, so you lost a guess:', get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

        # Input is good, play the game
        else:
            # Show user the outcome of their guess
            if guess in secret_word:
                letters_guessed.append(guess)
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(guess)
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                if guess in vowels:
                    guesses_remaining -= 2 # Remove two guesses for a wrong vowel guess
                else:
                    guesses_remaining -= 1 # Remove one guess for a wrong consonant guess


    # End game conditions
    print('------------')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is:', guesses_remaining * (count_unique + len(secret_word)))
    else:
        print('Sorry, you ran out of guesses, the word was', secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def hangman_with_help(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 8 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, you should reveal to the user one of the
      letters missing from the word at the cost of 2 guesses. If the user does
      not have 2 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    * If the guess is the symbol -, you should randomly select one of the
      available letters and add it to the set of guessed letters at no extra
      cost. This can only be done once per game.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    guesses_remaining = 8
    available_letters = string.ascii_lowercase
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f' ,'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    letters_guessed = []
    guess = ''
    warnings_left = 3
    freehint = 1
    freehintletter = ''

    count_unique = len(''.join(set(secret_word))) # get the number of unique characters in the secret_word

    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is',len(secret_word), 'letters long.')
    print('You have', warnings_left, "warnings left.")


    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
        print('------------')
        # Print how many guesses the user has left
        if guesses_remaining > 1:
            print('You have', guesses_remaining, 'guesses left.')
        else:
            print('You have', guesses_remaining, 'guess left.')
        print('Available letters:', get_available_letters(letters_guessed))

        # Get the user guess
        guess = get_input(letters_guessed)

        # When the guess is not a valid character
        if guess == 'invalid' and warnings_left > 0:
            warnings_left -= 1
            if warnings_left == 1:
                print('Oops! That is not a valid letter. You have', warnings_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That is not a valid letter. You have', warnings_left, 'warnings left:', get_guessed_word(secret_word, letters_guessed))

        elif guess == 'invalid' and warnings_left <= 0:
            print('Oops! That is not a valid letter. You have no warnings left, so you lost a guess:', get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

        # If the user wants a free hint
        elif guess == 'freehint':
            if freehint > 0:
                choose_from = available_help(secret_word, get_available_letters(letters_guessed))
                freehint_letter = choose_from[random.randint(0, len(choose_from) -1)]
                letters_guessed.append(freehint_letter)
                print('Letter revealed:', freehint_letter)
                freehint -= 1
            else:
                print('You have already used your free guess.')

        # If the user wants to spend guesses for a hint
        elif guess == 'help':
            if guesses_remaining > 1:
                choose_from = available_help(secret_word, get_available_letters(letters_guessed))
                exposed_letter = choose_from[random.randint(0, len(choose_from) - 1)]
                letters_guessed.append(exposed_letter)
                print('Letter revealed:', exposed_letter)
                guesses_remaining -= 2
            else:
                print('Sorry, you do not have enough guesses reamining!')

        # When the guess was already guessed before
        elif guess == 'priorguess' and warnings_left > 0:
            warnings_left -= 1
            if warnings_left == 1:
                print('Oops! You already guessed that letter. You have', warnings_left, 'warning left:', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! You already guessed that letter. You have', warnings_left, 'warnings left:', get_guessed_word(secret_word, letters_guessed))

        elif guess == 'priorguess' and warnings_left <= 0:
            print('Oops! You already guessed that letter. You have no warnings left, so you lost a guess:', get_guessed_word(secret_word, letters_guessed))
            guesses_remaining -= 1

        # Input is good, play the game
        else:
            # Show user the outcome of their guess
            if freehint == 0:
                print('You used your free guess on the letter', freehint_letter)
            if guess in secret_word:
                letters_guessed.append(guess)
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                letters_guessed.append(guess)
                if guess in vowels:
                    guesses_remaining -= 2 # Remove two guesses for a wrong vowel guess
                else:
                    guesses_remaining -= 1 # Remove one guess for a wrong consonant guess

    # End game conditions
    print('------------')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        print('Your total score for this game is:', guesses_remaining * (count_unique + len(secret_word)))
    else:
        print('Sorry, you ran out of guesses, the word was', secret_word)




# When you've completed your hangman_with_help function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_help(secret_word)
