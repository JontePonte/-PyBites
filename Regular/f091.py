
"""
Catching up after #PyCon2018 ... in this Bite you do multiple string matching. 
Complete contains_only_vowels, contains_any_py_chars, and contains_digits below. 
See more info in the docstrings and the tests. Have fun!
"""


VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    for char in input_str.lower():
        if char not in VOWELS:
            return False
    return True
    


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    for char in input_str.lower():
        if char in PYTHON:
            return True
    return False


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    for char in input_str:
        if char.isnumeric():
            return True
    return False


print(contains_only_vowels('aaiiuuee'))
print(contains_only_vowels('abababablklklcccc'))
print(contains_only_vowels('aaaaa1'))
print()
print(contains_any_py_chars('12357655954'))
print(contains_any_py_chars('ijuhijuhpooo'))
print(contains_any_py_chars('abababablklklcccc'))
print()
print(contains_digits('asdjahsuhcjskdf'))
print(contains_digits('asdjahsu9hcjskdf'))
print(contains_digits('12398735987'))
print()