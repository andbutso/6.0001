# Problem Set 4C
# Name: George Mu
# Collaborators:
# Time Spent: 1:00
# Late Days Used:

import string
import copy
from itertools import permutations

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

def get_permutations(characters):
    '''
    Generates all unique permutations of a sequence of characters.
    Duplicate permutations (resulting from a character that appears
    multiple times in the input) will be removed.

    For example:
    get_permutations('abc') -> ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    get_permutations('aa') -> ['aa']
    get_permutations('aba') -> ['aba', 'aab', 'baa']

    characters (string): a string containing a sequence of characters

    Returns: a list of strings corresponding to all unique permutations
    '''
    perms = [''.join(p) for p in permutations(characters)]
    return list(set(perms))

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object

        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
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

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled
        according to vowels_permutation. The first letter in vowels_permutation
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        self.vowels_permutation_lower = vowels_permutation
        self.vowels_permutation_upper = vowels_permutation.upper()
        self.transpose_dict = {}

        # Populate the transpose_dict with the vowel keys:
        for letter in VOWELS_LOWER:
            self.transpose_dict[letter] = ''

        self.transpose_dict['a'] = self.vowels_permutation_lower[0]
        self.transpose_dict['e'] = self.vowels_permutation_lower[1]
        self.transpose_dict['i'] = self.vowels_permutation_lower[2]
        self.transpose_dict['o'] = self.vowels_permutation_lower[3]
        self.transpose_dict['u'] = self.vowels_permutation_lower[4]

        for letter in VOWELS_UPPER:
            self.transpose_dict[letter] = ''

        self.transpose_dict['A'] = self.vowels_permutation_upper[0]
        self.transpose_dict['E'] = self.vowels_permutation_upper[1]
        self.transpose_dict['I'] = self.vowels_permutation_upper[2]
        self.transpose_dict['O'] = self.vowels_permutation_upper[3]
        self.transpose_dict['U'] = self.vowels_permutation_upper[4]


        # Populate the rest of the dictionary with the consonants

        for letter in CONSONANTS_UPPER:
            self.transpose_dict[letter] = letter
        for letter in CONSONANTS_LOWER:
            self.transpose_dict[letter] = letter

        return self.transpose_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary

        Returns: an encrypted version of the message text, based
        on the dictionary
        '''
        self.letters = string.ascii_lowercase + string.ascii_uppercase
        self.transpose_dict = transpose_dict
        self.encrypted_message_text = ''

        for letter in self.message_text:
            if letter in self.letters:
                self.encrypted_message_text += self.transpose_dict[letter]
            else:
                self.encrypted_message_text += letter

        return self.encrypted_message_text


class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message

        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.

        If no good permutations are found (i.e. no permutations result in
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message

        Hint: use get_permutations
        '''
        # Generate possible vowel permutations:
        self.vowel_permutations = get_permutations('aeiou')
        self.best_permutation = ''
        self.best_permutation_words = 0
        self.permutation_performance_history = {}

        # Test the number of valid words for each permutation and add it to self.permutation_performance_history
        for each_permutation in self.vowel_permutations:
            self.best_words_performance = 0
            self.test_dictionary = self.build_transpose_dict(each_permutation) # Build the dictionary for the given permutation
            self.decrypted_message = self.apply_transpose(self.test_dictionary) # Translate the message using the new dictionary

            # Test to see how many words in the decrypted_message are real words
            self.decrypted_message_elements = self.decrypted_message.split() # Split the message into a list with each word

            for word in self.decrypted_message_elements:
                if is_word(self.valid_words, word):
                    self.best_words_performance += 1

            self.permutation_performance_history[each_permutation] = self.best_words_performance

        # Test to see which permutation was the best
        for permutation in self.permutation_performance_history:
            if self.permutation_performance_history[permutation] > self.best_permutation_words:
                self.best_permutation = permutation # Set the best permutation to be the one we just tested
                self.best_permutation_words = self.permutation_performance_history[permutation] # Set the best performance equal to that of the one we just test_encrypted_submessag

        # Return the decrypted message
        self.decrypted_message = self.apply_transpose(self.build_transpose_dict(self.best_permutation))
        return self.decrypted_message





def test_submessage():
    '''
    Write two test cases for the SubMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

    message = SubMessage("aaaaaaaa!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "eeeeeeee!")
    print("Actual encryption:", message.apply_transpose(enc_dict))


    message = SubMessage("AEIOU")
    permutation = "EAiou"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "EAIOU")
    print("Actual encryption:", message.apply_transpose(enc_dict))



def test_encrypted_submessage():
    '''
    Write two test cases for the EncryptedSubMessage class here.
    Each one should handle different cases (see handout for
    more details.) Write a comment above each test explaining what
    case(s) it is testing.
    '''

    enc_message = EncryptedSubMessage('HAllu Wurld!')
    print("Expected decryption: HEllo World!")
    print("Actual decryption:", enc_message.decrypt_message())

    enc_message = EncryptedSubMessage('MAET!')
    print("Expected decryption: MEAT!")
    print("Actual decryption:", enc_message.decrypt_message())



if __name__ == '__main__':

    # Uncomment these lines to try running your test cases
    test_submessage()
    test_encrypted_submessage()

    pass
