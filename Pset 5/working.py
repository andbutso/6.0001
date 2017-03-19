import string
import re

phrase = 'PURPLE COW'
text = 'The purple cow is soft and cuddly.'

def is_phrase_in(phrase, text):

    # Lower the text characters, then return a list where each word is an element
    clean_text = re.findall(r"[\w']+", text.lower())
    # Lower the phrase characters, then return a list where each word is an element
    phrase = phrase.lower()
    phrase = phrase.split()

    # Then rejoin the elements into a phrase where every word is only separated by a single space
    # clean_text = " ".join(clean_text)
    # print("--------")
    # print(clean_text)

    # If the phrase is in the text, then return true
    print("--------")
    print(phrase)
    print(clean_text)
    print("--------")

    intersection = list(set(phrase) & set(clean_text))

    if phrase == intersection:
        print("True")
    else:
        print("False")




is_phrase_in(phrase, text)
