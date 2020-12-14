"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    
    letters = [letter.lower() for letter in word if letter.isalnum()]

    half_word_length = int(len(letters)/2)
    for n in range(0,half_word_length):
        # check if n-th letter from start == n-th letter from end
        if not letters[n] == letters[-(n+1)]:
            return False

    # return True if no tests said different
    return True


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""

    if words == None:
        words = load_dictionary()

    # filter palindroms
    palindroms = [word for word in words if is_palindrome(word)]

    # return longest palindrom
    return max(palindroms, key=len)
    


print(is_palindrome('halooåoolah'))
print(get_longest_palindrome(['ama','samomas','ydgodfhkleifje','tittit']))