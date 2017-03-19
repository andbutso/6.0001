# Problem Set 4B
# Name: George Mu
# Collaborators:
# Time Spent: 3:30
# Late Days Used:

import string
import copy

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determi ned by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        self.safe_valid_words = copy.deepcopy(self.valid_words)
        return self.safe_valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift.

        The dictionary should have 52 keys of all the uppercase letters and
        all the lowercase letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping letter (string) to
                 another letter (string).
        '''

        self.shift = shift
        self.shift_amount = self.shift % 26
        self.letters = string.ascii_lowercase + string.ascii_uppercase

        # Create the lower Cipher dictionary
        self.plain_lower = string.ascii_lowercase
        self.plain_lower_double = 2 * self.plain_lower
        self.cipher_lower = {}
        for letter in self.plain_lower:
            self.cipher_lower[letter] = self.plain_lower_double[self.plain_lower_double.find(letter) + self.shift_amount]

        # Create the upper cipher dictionary
        self.plain_upper = string.ascii_uppercase
        self.plain_upper_double = 2 * self.plain_upper
        self.cipher_upper = {}
        for letter in self.plain_upper:
            self.cipher_upper[letter] = self.plain_upper_double[self.plain_upper_double.find(letter) + self.shift_amount]

        # Join the two dictionaries

        self.encryption_dict = self.cipher_lower.copy()
        self.encryption_dict.update(self.cipher_upper)

        return self.encryption_dict

    def apply_shift(self, shift_dict):
        '''
        Applies the Caesar Cipher to self.message_text with letter shifts
        specified in shift_dict. Creates a new string that is self.message_text,
        shifted down the alphabet by some number of characters, determined by
        the shift value that shift_dict was built with.

        shift_dict: a dictionary with 52 keys, mapping lowercase and uppercase
            letters to their new letters (as built by build_shift_dict)

        Returns: the message text (string) with every letter shifted using the
            input shift_dict

        '''
        self.shift_dict = shift_dict
        self.encrypted_message_text = ''

        # Take every character in the message text. If character is a letter, then shift it. Otherwise, keep it the same (i.e. don't do anything to punctuation and grammar)
        for letter in self.message_text:
            if letter in self.letters:
                self.encrypted_message_text += self.shift_dict[letter]
            else:
                self.encrypted_message_text += letter

        return self.encrypted_message_text



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object.

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message. It has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.encrypted_message_text (string, encrypted using self.encryption_dict)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words("words.txt")
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''

        return copy.deepcopy(self.encryption_dict)

    def get_encrypted_message_text(self):
        '''
        Used to safely access self.encrypted_message_text outside of the class

        Returns: self.encrypted_message_text
        '''
        return self.encrypted_message_text

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage, and updates any other
        attributes that are determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift

        # Update the attributes that are derived from shift
        self.encryption_dict = self.build_shift_dict(self.shift)
        self.encrypted_message_text = self.apply_shift(self.encryption_dict)



class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object inherits from Message. It has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.message_text = text
        self.valid_words = load_words("words.txt")

    def decrypt_message(self):
        '''
        Decrypts self.message_text by trying every possible shift value
        and finding the "best" one.
        We will define "best" as the shift that creates the maximum number of
        valid English words when we use apply_shift(shift)on the message text.
        If s is the original shift value used to encrypt the message, then we
        would expect (26 - s) to be the best shift value for decrypting it.

        Note: if multiple shifts are equally good, such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return.

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # Test each shift key for the results
        self.shift_key = 0 # Start the shift key at 0
        self.shift_results = {} # initialize a dictionary containing the shift key and the number of valid words
        self.best_shift_key = 0
        self.best_shift_words = 0

        while self.shift_key < 27: # For each of the possible shift keys 0 - 26
            # Initialize the starting variables
            self.test_message_elements = []

            # generate the new shift_dict using the shift_key
            self.test_dict = self.build_shift_dict(self.shift_key)

            # apply the new shift_dict to self.message text
            self.test_message = self.apply_shift(self.test_dict)

            # Convert the new message text into a list where each word is an element
            self.test_message_elements = self.test_message.split()

            # Test to see how many of the elements in test_words are a word
            self.word_counter = 0

            for word in self.test_message_elements:
                if is_word(self.valid_words, word):
                    self.word_counter += 1

            # Put the results in a dictionary
            self.shift_results[self.shift_key] = self.word_counter

            # Increment the shift key
            self.shift_key += 1

        # See which key has the best results
        for s in self.shift_results:
            if self.shift_results[s] > self.best_shift_words:
                self.best_shift_words = self.shift_results[s]
                self.best_shift_key = s


        # Return the tuple
        self.test_dict = self.build_shift_dict(self.best_shift_key)
        self.decrypted_message = self.apply_shift(self.test_dict)
        return (self.best_shift_key, self.decrypted_message)

def test_plaintext_message():
    '''
    Write two test cases for the PlaintextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (PlaintextMessage) #####

#    # This test is checking encoding a lowercase string with punctuation in it.
#    plaintext = PlaintextMessage('hello!', 2)
#    print('Expected Output: jgnnq!')
#    print('Actual Output:', plaintext.get_encrypted_message_text())

    # Test 1 to see if it handles wraparound shift key appropriately
    test1 = PlaintextMessage('George!!!', 27)
    print('Expected Output: Hfpshf!!!')
    print('Actual Output:', test1.get_encrypted_message_text())

    # Test 2 to see if it handles negative shit key appropriately
    test2 = PlaintextMessage('George!!!', -1)
    print('Expected Output: FdnqFd!!!')
    print('Actual Output:', test2.get_encrypted_message_text())





def test_ciphertext_message():
    '''
    Write two test cases for the CiphertextMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

#    #### Example test case (CiphertextMessage) #####

#   # This test is checking decoding a lowercase string with punctuation in it.
#    ciphertext = CiphertextMessage('jgnnq!')
#    print('Expected Output:', (24, 'hello!'))
#    print('Actual Output:', ciphertext.decrypt_message())

    # Test if it can decode all caps
    test3 = CiphertextMessage('BZQS')
    print('Expected Output:', (1, 'CART'))
    print('Actual Output:', test3.decrypt_message())

    # Test if it can decode a string where words are separated by dashes
    test4 = CiphertextMessage('ij nf')
    print('Expected Output:', (25, 'hi-me'))
    print('Actual Output:', test4.decrypt_message())

def decode_story():
    '''
    Write your code here to decode the story contained in the file story.txt.
    Hint: use the helper function get_story_string and your CiphertextMessage class.

    Returns: a tuple containing (best_shift, decoded_story)

    '''
    story = CiphertextMessage(get_story_string())
    return story.decrypt_message()

if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_plaintext_message()
    test_ciphertext_message()

    # Uncomment these lines to try running decode_story_string()
    best_shift, story = decode_story()
    print("Best shift:", best_shift)
    print("Decoded story: ", story)
